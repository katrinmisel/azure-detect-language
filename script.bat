@echo off

set /p text=Text:
curl "%Cognitive_endpoint%" -H "Ocp-Apim-Subscription-Key: %Cognitive_API%" -H "Ocp-Apim-Subscription-Region:%Cognitive_region%" -H "Content-Type: application/json" -d "[{'Text':'%text%'}]"\\
echo.

cmd /k
