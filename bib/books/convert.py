import os			    # for magick and tesseract commands
import time			  # for epoch time
import calendar 	# for epoch time
from PyPDF2 import PdfFileMerger
import shutil

epoch_time = int(calendar.timegm(time.gmtime()))

def convert(file):
	aux = file.rsplit('/', 1) # split the path and the file name
	path_file = aux[0]
	file = aux[1]
	for f in os.listdir(path_file):			
		if file == f:
			path_file = path_file + '/'
			if file.endswith('.pdf'): # if it is a PDF, use it 
				file = file.lower().replace('.pdf', '') # get just the filepath without the extension				
				folder = path_file + str(int(epoch_time)) + '_' + file # generate a folder name for temporary images
				combined = folder + '/' + file # come up with temporary export path
				
				# create folder
				if not os.path.exists(folder): # make the temporary folder
					os.makedirs(folder)	

				print('convert PDF to PNG(s)')
				# convert PDF to PNG(s)
				magick = 'convert -density 150 "' + path_file + file + '.pdf" -colorspace RGB "' + combined + '-%04d.png"'
				os.system(magick)

				# convert PNG(s) to PDF(s) with OCR data
				pngs = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
				for pic in pngs:
					if pic.endswith('.png'):
						combined_pic = folder + '/' + pic
						tesseract = 'tesseract "' + combined_pic + '" "' + combined_pic + '-ocr" -l por PDF'
						os.system(tesseract)
				
				# combine OCR'd PDFs into one
				ocr_pdfs = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

				merger = PdfFileMerger()
				for pdf in ocr_pdfs:
					if pdf.endswith('.pdf'):
						merger.append(folder + '/' + pdf)

				merger.write(path_file + file + '-ocr.pdf')		
				merger.close()
				shutil.rmtree(folder) # remove the temporary folder and its files
				os.remove(path_file + file + '.pdf') # remove the old file
				os.rename(os.path.join(path_file, file + '-ocr.pdf'), os.path.join(path_file, file + '.pdf')) # rename the new file			
