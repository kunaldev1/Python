<br clear="both">

<div data-importer="border">
  <img style="100%" src="https://capsule-render.vercel.app/api?type=egg&section=header&reversal=false&text=Welcome&fontSize=64&fontColor=FFFFFF&fontAlign=50&fontAlignY=50&stroke=-&animation=scaleIn&descSize=21&descAlign=50&descAlignY=50&textBg=false&color=gradient"  />
</div>

###

<br clear="both">

<h1 data-importer="text" align="center">Hey 👋 What's up?</h1>

###

<br clear="both">

<h6 data-importer="text" align="left">🙎  My name is Kunal Jha <br> 🧑🏼‍🎓 I'm a Student <br> 📌Location: Janakpur dham-04, Nepal.</h6>

###

<h2 data-importer="text" align="left">About me</h2>

###

<img data-importer="image" align="right" height="150" src="https://i.imgflip.com/65efzo.gif"  />

###

<h6 data-importer="text" align="left">✨ Creating bugs since my first program <br> 📚 I'm currently learning HTML, Java, C, Python, and SQL <br> 🐍 Python is the language I enjoy the most, especially for problem-solving and building practical projects <br>🎯 Goals: master Python, improve my development skills, and create real-world applications <br>🎲 Fun fact: if a task can be simplified with code, I want to try it</h6>

###

<h2 data-importer="text" align="left">I code with</h2>

###

<br clear="both">

<div data-importer="techs" align="center">
  <img src="https://cdn.simpleicons.org/python/3776AB" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://skillicons.dev/icons?i=c" height="40" alt="c logo"  />
  <img width="12" />
  <img src="https://cdn.simpleicons.org/html5/E34F26" height="40" alt="html5 logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="40" alt="css logo"  />
  <img width="12" />
  <img src="https://skillicons.dev/icons?i=js" height="40" alt="javascript logo"  />
  <img width="12" />
  <img src="https://skillicons.dev/icons?i=java" height="40" alt="java logo"  />
  <img width="12" />
  <img src="https://cdn.simpleicons.org/mysql/4479A1" height="40" alt="mysql logo"  />
  <img width="12" />
  <img src="https://skillicons.dev/icons?i=php" height="40" alt="php logo"  />
  <img width="12" />
  <img src="https://skillicons.dev/icons?i=nodejs" height="40" alt="nodejs logo"  />
  <img width="12" />
  <img src="https://skillicons.dev/icons?i=react" height="40" alt="react logo"  />
  <img width="12" />
  <img src="https://skillicons.dev/icons?i=blender" height="40" alt="blender logo"  />
  <img width="12" />
  <img src="https://skillicons.dev/icons?i=ai" height="40" alt="adobeillustrator logo"  />
</div>

###

<h2 data-importer="text" align="left">Social Media Links</h2>

###

<br clear="both">

<div data-importer="socials" align="left">
  <a href="https://www.linkedin.com/in/kunal-jha-698647370/" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/linkedin/default.svg" width="52" height="40" alt="linkedin logo"  />
  </a>
  <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/facebook/default.svg" width="52" height="40" alt="facebook logo"  />
  <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/telegram/default.svg" width="52" height="40" alt="telegram logo"  />
</div>

###

<img data-importer="snake" align="right" height="150" src="https://i.imgflip.com/65efzo.gif"  />

###

// pos is the PacMan image position variable- it is set to 0 initially
var pos = 0;
//pageWidth is the width of the webpage. This is later used to calculate when Pac-Man needs to turn around. 
let pageWidth = window.innerWidth;
//This array contains all the PacMan movement images
const pacArray = [
  ['PacMan1.png', 'PacMan2.png'],
  ['PacMan3.png', 'PacMan4.png'],
];

// this variable defines what direction should PacMan go into:
// 0 = left to right
// 1 = right to left (reverse)
var direction = 0;

// This variable helps determine which PacMan image should be displayed. It flips between values 0 and 1
var focus = 0;

// This function is called on mouse click. Every time it is called, it updates the PacMan image, position and direction on the screen.
function Run() {
  let img = document.getElementById('PacMan');
  let imgWidth = img.width;
  focus = (focus + 1) % 2;
  direction = checkPageBounds(direction, imgWidth, pos, pageWidth);
  img.src = pacArray[direction][focus];
  if (direction) {
    pos -= 20;
    img.style.left = pos + 'px';
  } else {
    pos += 20;
    img.style.left = pos + 'px';
  }
}
// TODO: Add a Javascript setInterval() method that will call the Run() function above every 200 milliseconds. Note: in the video, Dr. Williams uses the setTimeout() method, but here we are going to use a slightly different
// method called setInterval(), so that you can have practice using this method.
setInterval(Run, 150);

// Inside of the Run() function you will also have to add an extra argument "pageWidth", which is declared on line 4 when you call the checkPageBounds() function below. 

// This function determines the direction of PacMan based on screen edge detection. 
function checkPageBounds(direction, imgWidth, pos, pageWidth) {
  // TODO: Complete this to reverse direction upon hitting screen edge
  if (direction == 0 && pos + imgWidth >= pageWidth) direction = 1;
  if (direction == 1 && pos < 0) direction = 0;

  return direction;
}

//Please do not change
module.exports = checkPageBounds;


###

<div data-importer="profile-views" align="center">
  <img data-importer="profile-views" src="https://visitor-badge.laobi.icu/badge?page_id=kunaldev1.kunaldev1&"  />
</div>

###

<div data-importer="border">
  <img style="100%" src="https://capsule-render.vercel.app/api?type=egg&height=100&section=footer&reversal=true&fontSize=70&fontColor=FFFFFF&fontAlign=50&fontAlignY=50&stroke=-&descSize=20&descAlign=50&descAlignY=50&textBg=false&color=gradient"  />
</div>

###
