const video = document.getElementById("slideframe");
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
  current_video = n;
  video.src = vid_data[n].path + vid_data[n].filename;
  video.contentWindow.location.reload();
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

// run this at start
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

