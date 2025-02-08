<h1 align="center">Hi there, I'm <a href="https://github.com/andrejevdenis" target="_blank">Denis</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Computer science student</h3>

<h3 align="left">My stack:</h3>

![Python](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Python.svg)
![Pytest](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Pytest.svg)
![IntelliJ IDEA](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/IntelliJ_IDEA.svg)
![PyCharm](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/PyCharm.svg)
![Git](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Git.svg)
![Jenkins](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/jenkins.svg)
![Postman](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Postman.svg)
![Swagger](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Swagger.svg)
![Jira](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/jira.svg)
![Confluence](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/confluence.svg)
![ElasticSearch](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/ElasticSearch.svg)
![Grafana](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/grafana.svg)
![MySQL](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/mysql.svg)
![Postgres](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/postgres.svg)
![Windows](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Windows.svg)
![Android](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Android.svg)
![Ubuntu](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Ubuntu.svg)
![Firefox](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Firefox.svg)
![Google Chrome](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Google_Chrome.svg)
![IE](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Internet_Explorer.svg)
![Opera](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Opera.svg)
![Tor](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Tor.svg)
![Adobe Premiere Pro](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Adobe_Premiere_Pro.svg)
![Adobe Photoshop](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/adobe_photoshop.svg)
![Notepad++](https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Notepad.svg)

## Table of Contents
- [About](#-about)
- [Objects for test](#-objects-for-test)
- [How to Build](#-how-to-build)
- [Example of a report](#%EF%B8%8F-example-of-a-report)
- [Summary](#-summary)
- [Contacts](#%EF%B8%8F-contacts)


## 🚀 About 
I'm **AQA Engineer**, born in 1986 Samara, Russia, here is some facts about me and my QA experience:

- **Education**: 

    2008 - graduated from [The International Market Institute](https://www.imi-samara.ru/), faculty of Economics and Management, specialization in finance and credit.

    2016 - graduated from [City Business School](https://e-mba.ru/catalog/mini-mba), Mini-MBA Professional program, specialization logistics management.  

    2020 - graduated from [Yandex Practicum](https://practicum.yandex.ru/) courses "Test engineer"

    2024 - graduated from [QA-Guru](https://qa.guru/) courses "Python test automation"
- **My QA manual experience**: 

    In 2020 i had my first experience in testing acquired as a tester-assistant in [Yandex](https://yandex.ru/company). 
 
    From 2022 worked in [AvantLab](https://avantlab.ru/) on position JuniorQA, there i gained skills in working with Postman, Git, Jankins, Confluense, Postgress etc. 

    Having gained a certain experience, i been able to get a position of MiddleQA in [AO-RR](https://ao-rr.ru/#main__slider), from 04.2024.
- **My AQA experience**: After i graduated from [QA-Guru](https://qa.guru/) courses i started apply automation at work

# <h1 align="center">Takamul Autotst project</h1> 
## 🎯 Objects for test
- Fill and send contact form, positive test
- Fill and send contact form, negative test
- Take some path from main page to check some buttons that java scripts work right and redirects is correct.
- Asserts Digital Projects table [content](https://www.takamul.net.sa/services/digital-experience/digital-strategy) and buttons that should change it

## 📝 How to Build

To build autotests in Jenkins:
1. Open [project](https://jenkins.autotests.cloud/job/Takamul_proj/)
2. Choose Build with parameters
3. If necessary, change the parameters by selecting values from lists
4. Push Build
5. The result of starting the assembly can be viewed in the Allure report

>Features for this test in Jenkins:  
Website https://www.takamul.net.sa is heavy and if i try run it remotely by Chrome browser on https://selenoid.autotests.cloud it must be windowed on 320x480 size and it takes much more time for each iteration.  
Because of it the test setuped for Firefox browser.

To build the test local follow these steps:
```shell
# Open a terminal (Command Prompt or PowerShell for Windows, Terminal for macOS or Linux)

# Ensure Git is installed
# Visit https://git-scm.com to download and install console Git if not already installed

# Clone the repository
git clone https://github.com/andrejevdenis/Takamul_proj

# Download last version of Allure
https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/

# Set up it to main folder of project, rename like "allure"
cd ..\Takamul_proj\allure

# For run it by local browser, apply the specified features in conftest.py
# Run project to build first allure report
pytest tests

# Build allure report
allure/bin/allure.bat serve tests/allure-results

# Troubleshooting 

1. Check installed python packages. Use pip install for packages from requirements.txt
2. Check path environment variable windows
```
## ▶️ Example of a report
### Allure report generated
<img src="https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Allure1.png" width="630" height="320"/>

### Test statistics collected, bugs localized
<img src="https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Allure2.png" width="630" height="320"/>

### Attached is a video of the test
<img src="https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Allure3.gif" width="630" height="320"/>

### Notification received of Jenkins build results in Telegram bot
<img src="https://github.com/andrejevdenis/Takamul_proj/blob/master/Icons/Telegram.png" width="350" height="320"/>

## 📈 Summary
First test is just an example of valid test. I fill an incorrect email in order not to clog the production. But it passed! And here we go to interesting part of my test...  
Second and third shows bugs on https://www.takamul.net.sa
If i truly worked on it, for failed autotests i go there and manually locate this bug, check what can be wrong else? And then i can create a bug report for developers/

## 🗨️ Contacts

For more details about my experience, services, or any general information, feel free to reach out to me. Below are the best ways to contact:

- **Email**: Send your inquiries at [andrejevdenis00@gmail.com](mailto:andrejevdenis00@gmail.com).
- **Telegram**: Also you can call me or send a message at [t.me/DenisAKtrue](https://t.me/DenisAKtrue).

Looking forward to assisting you and ensuring your business with me is successful and enjoyable!

[Back to top](#top)
