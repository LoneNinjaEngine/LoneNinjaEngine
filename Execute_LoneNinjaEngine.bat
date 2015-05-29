@ECHO OFF

	IF EXIST LoneNinjaEngine.py. (
		echo Starting the LoneNinja Execution
		echo 	
		IF EXIST inputfile.txt. (
			
			IF EXIST rt-polaritydata (
				python LoneNinjaEngine.py
			) ELSE (
				echo  rt-polaritydata directory is missing, EXITING
				echo  
				echo  
				PAUSE
				@exit
			)
			
		) ELSE (
			echo  inputfile.txt file is missing, EXITING
			echo  
			echo  
			PAUSE
			@exit
		)
		
	) ELSE (
		echo  LoneNinjaEngine.py file is missing, EXITING
		echo  
		echo  
		PAUSE
		@exit
	)
echo  
echo  
echo  
set /p FLAG= Do you want load the feed text into Repository {Y/N}:	

GOTO; %FLAG%

:N
	echo EXITING from LoneNinja Engine Update Execution
	echo
	echo
	PAUSE
	@exit
:Y
	IF EXIST LoneNinjaEngineUpdater.py. (
		echo Starting the LoneNinjaEngineUpdater Execution
		echo	
		IF EXIST inputfile.txt. (
			IF EXIST outputfile.txt (
				
				IF EXIST rt-polaritydata (
					python LoneNinjaEngineUpdater.py
				) ELSE (
					echo  rt-polaritydata directory is missing, EXITING
					echo
					echo
					PAUSE
					@exit
				)
			) ELSE (
				echo  outputfile.txt file is missing, EXITING
				echo  
				echo  
				PAUSE
				@exit	
			)
			
		) ELSE (
			echo  inputfile.txt file is missing, EXITING
			echo  
			echo  
			PAUSE
			@exit
		)
		
	) ELSE (
		echo  LoneNinjaEngine.py file is missing, EXITING
		echo  
		echo  
		PAUSE
		@exit
	)

PAUSE
