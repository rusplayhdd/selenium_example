		IN WINDOWS OS use THE PowerShell !!!

1) Перед тем как начать писать тесты на SELENIUM создаем в директрии VirtualEnv, 
	use the comands:
	python -m venv {env_name}

2) Создаем в директории файлик .gitignore and write dawn in the file {env_name}\  
	
3) ДАЛЕЕ необходимо активировать virt_env use the folowing:
	.\{env_name}\Scripts\activate.bat or .ps1
	
4) Далее устанавливаем библиотеки:
	pip install pytest
	pip install selenium
 	pip install webdriver-manager
 	pip install allure-pytest

5) For start the allure use:
	pytest --alluredir <folder_name>
   
5.1) To open a dashboard:
	npx allure-commandline serve <folder_name>
