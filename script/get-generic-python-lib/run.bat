IF NOT DEFINED CM_TMP_CURRENT_SCRIPT_PATH SET CM_TMP_CURRENT_SCRIPT_PATH=%CD%

%CM_PYTHON_BIN_WITH_PATH% %CM_TMP_CURRENT_SCRIPT_PATH%\detect-version.py
IF %ERRORLEVEL% NEQ 0 EXIT 1