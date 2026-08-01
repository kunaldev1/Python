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

<img data-importer="snake" align="right" height="150" src="[https://i.imgflip.com/65efzo.gif](https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake.svg)"  />

npx generate-snake-animation@3 --forgejo_user codeberg.org/JasterV --output snake.svg?palette=codeberg
name: generate animation

on:
  # run automatically every 24 hours
  schedule:
    - cron: "0 */24 * * *" 
  
  # allows to manually run the job at any time
  workflow_dispatch:
  
  # run on every push on the master branch
  push:
    branches:
    - master
    
  

jobs:
  generate:
    permissions: 
      contents: write
    runs-on: ubuntu-latest
    timeout-minutes: 5
    
    steps:
      # generates a snake game from a github user (<github_user_name>) contributions graph, output a svg animation at <svg_out_path>
      - name: generate github-contribution-grid-snake.svg
        uses: Platane/snk/svg-only@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark
          
          
      # push the content of <build_dir> to a branch
      # the content will be available at https://raw.githubusercontent.com/<github_user>/<repository>/<target_branch>/<file> , or as github page
      - name: push github-contribution-grid-snake.svg to the output branch
        uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
###

<div data-importer="profile-views" align="center">
  <img data-importer="profile-views" src="https://visitor-badge.laobi.icu/badge?page_id=kunaldev1.kunaldev1&"  />
</div>

###

<div data-importer="border">
  <img style="100%" src="https://capsule-render.vercel.app/api?type=egg&height=100&section=footer&reversal=true&fontSize=70&fontColor=FFFFFF&fontAlign=50&fontAlignY=50&stroke=-&descSize=20&descAlign=50&descAlignY=50&textBg=false&color=gradient"  />
</div>

###
