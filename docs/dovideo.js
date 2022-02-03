const video = document.getElementById("thevideo");
const title = document.getElementById("thetitle");
const toc = document.getElementById("toc-list");

const vid_data = [
  {
    "title": "Allgemeines Binom",
    "timestamps": [
      3.499999999999998,
      4.499999999999995,
      5.499999999999991,
      6.499999999999988,
      7.499999999999984,
      8.500000000000007
    ],
    "filename": "Allgemein.mp4",
    "path": "videos/"
  },
  {
    "title": "Third Binomial Formula",
    "timestamps": [
      1.0000000000000013,
      2.9999999999999942,
      3.9999999999999907,
      4.999999999999988,
      5.999999999999984,
      6.9999999999999805,
      13.000000000000076,
      16.000000000000224,
      17.000000000000167
    ],
    "filename": "BinomDrei.mp4",
    "path": "videos/"
  },
  {
    "title": "Animation of the binomal formula",
    "timestamps": [
      1.0000000000000013,
      1.9999999999999978,
      2.9999999999999942,
      3.9999999999999907,
      6.9999999999999805,
      12.000000000000176
    ],
    "filename": "BinomEins.mp4",
    "path": "videos/"
  },
  {
    "title": "Second Binomial Formula",
    "timestamps": [
      1.0000000000000013,
      1.9999999999999978,
      2.9999999999999942,
      3.9999999999999907,
      4.999999999999988,
      10.000000000000034,
      16.00000000000018,
      22.00000000000001
    ],
    "filename": "BinomZwei.mp4",
    "path": "videos/"
  },
  {
    "title": "Seerosenteich",
    "timestamps": [
      1.0000000000000013,
      1.9999999999999978,
      2.9999999999999942,
      3.9999999999999907,
      4.999999999999988,
      5.999999999999984,
      6.9999999999999805
    ],
    "filename": "Teich.mp4",
    "path": "videos/"
  },
  {
    "title": "Reflections of Linear Functions",
    "timestamps": [
      0,
      2.0,
      5.0,
      11.0,
      12.0,
      19.0,
      20.0,
      27.0,
      28.0,
      29.0
    ],
    "filename": "Linear.mp4",
    "path": "videos/"
  },
  {
    "title": "Potenzfunktionen",
    "timestamps": [
      0,
      1.0000000000000013,
      1.9999999999999978,
      2.9999999999999942,
      3.9999999999999907,
      4.999999999999988,
      5.999999999999984,
      6.9999999999999805,
      7.999999999999977,
      9.000000000000027,
      10.000000000000076,
      11.000000000000126,
      12.000000000000176,
      13.000000000000226
    ],
    "filename": "Potenz.mp4",
    "path": "videos/"
  },
  {
    "title": "Animation of the Newton method",
    "timestamps": [
      0,
      1.9999999999999978,
      3.9999999999999907,
      5.999999999999984,
      7.999999999999977
    ],
    "filename": "Newton.mp4",
    "path": "videos/"
  },
  {
    "title": "Zahlenmengen",
    "timestamps": [
      2.9999999999999942,
      5.999999999999984,
      12.133333333333516,
      27.133333333333255
    ],
    "filename": "Numbersets.mp4",
    "path": "videos/"
  }
];
var current_stamp = 0;
var current_video = 0;

function get_parameters() {
  params = new URLSearchParams(window.location.search);
  dest = parseInt(params.get("anim"));
  if (isNaN(dest)) {
    return 0;
  }
  return 0 <= dest & dest < vid_data.length ? dest : 0;
}
current_video = get_parameters();

function load_video(n){
  // n specifies the index in the vid_data.
  current_stamp = 0;
  current_video = n;
  video.src = vid_data[n].path + vid_data[n].filename;
  video.currentTime = vid_data[n].timestamps[current_stamp];
  video.load();
  title.innerHTML = vid_data[n].title;
}

load_video(current_video);

function populate_toc(){
  for (var i=0; i < vid_data.length; i++){
    x = vid_data[i];
    newli = document.createElement("li");
    newli.id = i;
    // TODO: need to somehow save the value of i here?
    newli.onclick = function(){load_video(this.id)};
    newli.innerHTML = x.title;
    toc.appendChild(newli);
  }
  toc.lastChild.classList.add("last");
}
populate_toc();

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

document.addEventListener('keydown', logKey);
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
