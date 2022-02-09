const video = document.getElementById("thevideo");
const title = document.getElementById("thetitle");
const toc = document.getElementById("toc-list");
const colls = document.getElementsByClassName("collapsible")

function get_parameters() {
  params = new URLSearchParams(window.location.search);
  dest = parseInt(params.get("anim"));
  if (isNaN(dest)) {
    return 0;
  }
  return 0 <= dest & dest < vid_data.length ? dest : 0;
}

function load_video(n){
  // n specifies the index in the vid_data.
  current_stamp = 0;
  current_video = n;
  video.src = vid_data[n].path + vid_data[n].filename;
  video.currentTime = vid_data[n].timestamps[current_stamp];
  video.load();
  title.innerHTML = vid_data[n].title;
}

function populate_toc(){
  for (var i=0; i < vid_data.length; i++){
    x = vid_data[i];
    newli = document.createElement("li");
    newli.id = i;
    // TODO: need to somehow save the value of i here?
    newli.onclick = function(){
      load_video(this.id);
      var tocdiv = document.getElementById("toc");
      var tocbutton = document.getElementById("toc-button");
      tocdiv.style.maxHeight = null;
      tocbutton.classList.toggle("active");
    };
    newli.innerHTML = x.title;
    toc.appendChild(newli);
  }
}

function load_prev_timestamp(){
  if (current_stamp > 0) {
    current_stamp--;
  } else {
    video.currentTime = 0;
  }
  video.currentTime = vid_data[current_video].timestamps[current_stamp];
}

function play_to_next_timestamp(){
  function checktime(){
    if (video.currentTime > vid_data[current_video].timestamps[current_stamp]){
      video.pause();
    } else {
      setTimeout(checktime, 50);
    }
  }
  video.currentTime = vid_data[current_video].timestamps[current_stamp]
  current_stamp++
  if (current_stamp >= vid_data[current_video].timestamps.length){
    current_stamp=0
  }
  video.play()
  checktime();
}

function playPause() {
  if (video.paused) {
    video.play();
  } else {
    video.pause();
  }
}

function logKey(e) {
  switch (e.code) {
    case "ArrowRight":
      play_to_next_timestamp();
      break;
    case "ArrowLeft":
      load_prev_timestamp();
      break;
    case "Space":
    case "Enter":
      playPause();
      break;
    case "KeyF":
      video.requestFullscreen();
      break;
    default:
      console.log("unknown key code: " + e.code);
  }
}

// run this at start
var current_stamp = 0;
var current_video = get_parameters();
load_video(current_video);

populate_toc();
// enable collapsing
const tbutton = document.getElementById("toc-button");
tbutton.addEventListener("click", function() {
  this.classList.toggle("active");
  var content = this.nextElementSibling;
  if (content.style.maxHeight){
    content.style.maxHeight = null;
  } else {
    content.style.maxHeight = content.scrollHeight + "px";
  } 
});
// add keyboard shortcuts
document.addEventListener('keydown', logKey);
