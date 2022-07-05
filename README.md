<div id="top"></div>


[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/MaharshPatelX/Auto-Bday-wisher">
    <img src="https://github.com/MaharshPatelX/Auto-Bday-wisher/blob/main/Images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">AUTO Bday Wisher</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/MaharshPatelX/Auto-Bday-wisher"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/MaharshPatelX/Auto-Bday-wisher">View Demo</a>
    ·
    <a href="https://github.com/MaharshPatelX/Auto-Bday-wisher/issues">Report Bug</a>
    ·
    <a href="https://github.com/MaharshPatelX/Auto-Bday-wisher/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

In this days it is normal to forget 'Birthdays'. Our application will help you to wish your friend and family member's Birthday.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With :

* [Python](https://www.python.org/)
* [Tkinter](https://pypi.org/project/tk-tools/)
* [MongoDB](https://www.mongodb.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites :

- You need to install Python first .


### Installation :


1. Clone the repo
   ```sh
   git clone https://github.com/MaharshPatelX/Auto-Bday-wisher.git
   ```

2. Install Python packages
   ```sh
    pip install instabot
    pip install tk-tools
    pip install pymongo
    pip install pymongo[srv]
    pip install bson

3. Add 'makejson.py' and 'message.py' fileOn SERVER(raspberry pi) side <br> Change MonogoDB URL and Instagram Username - Password
<br><br>

   ```python
    # makejson.py
    7. myclient = pymongo.MongoClient("Your-MongoDB-URL")
    
    # message.py
    7. bot.login(username="user", password="pass", use_cookie = False)
   ```

4. Run Files On SERVER(raspberry pi) side
   ```sh
   python makejson.py
   python message.py
   ```
5. To add Birth dates and Instagram IDs Run 'app.py'
   ```sh
   python app.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Gmail: maharsh2017@gmail.com
<br>
Project Link: [https://github.com/MaharshPatelX/Auto-Bday-wisher](https://github.com/MaharshPatelX/Auto-Bday-wisher)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/MaharshPatelX/Auto-Bday-wisher/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/MaharshPatelX/Auto-Bday-wisher/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/MaharshPatelX/Auto-Bday-wisher/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/MaharshPatelX/Auto-Bday-wisher/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/MaharshPatelX/Auto-Bday-wisher/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/maharsh-patel-4a8261177/
[product-screenshot]: https://github.com/MaharshPatelX/Auto-Bday-wisher/blob/main/Images/home.PNG
