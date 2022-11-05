
// creating square
var colors = ['#fc45cd', '#cc002a', '#ff099a', '#ff00e4', '#ff0808', '#b300ff', '#6f00ff', '#009fff', '#00ffe2', '#00fba0', '#00ff73', '#00ff3b', '#2ccb13', '#aff70d', '#f808ff', '#ff6a00', '#a600ff','#0000ff', '#00d4ff', '#23ff00', '#008aff', '#ff00c6', '#67ff73', '#f1ff0c', '#ff67dd', '#ff000'];
var boxes = document.querySelectorAll(".card-color");

for (i = 0; i < boxes.length; i++) {
  // Pick a random color from the array 'colors'.
  boxes[i].style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
//   boxes[i].style.width = '100px';
//   boxes[i].style.height = '100px';
  boxes[i].style.display = 'inline-block';
}

var color = localStorage.getItem("color");