@echo on

cd "C:\Users\chinjooern\Desktop\TR\WORN RAIL"

"C:\Users\chinjooern\AppData\Local\Continuum\anaconda3\python.exe" "C:\Users\chinjooern\Desktop\TR\WORN RAIL\COMBINE EXCEL FILES (WORN RAIL).py"

cd "C:\Users\chinjooern\Desktop\TR\RAILS AND CABLES"

"C:\Users\chinjooern\AppData\Local\Continuum\anaconda3\python.exe" "C:\Users\chinjooern\Desktop\TR\RAILS AND CABLES\COMBINE RAILS AND CABLES MASTERLISTS.py"

cd "C:\Users\chinjooern\Desktop\TR\ADD-ONS"

"C:\Users\chinjooern\AppData\Local\Continuum\anaconda3\python.exe" "C:\Users\chinjooern\Desktop\TR\ADD-ONS\PLATFORM_MATCHING.py"

"C:\Users\chinjooern\AppData\Local\Continuum\anaconda3\python.exe" "C:\Users\chinjooern\Desktop\TR\ADD-ONS\DEFECT_MATCHING (BINARY SEARCH).py"

"C:\Users\chinjooern\AppData\Local\Continuum\anaconda3\python.exe" "C:\Users\chinjooern\Desktop\TR\ADD-ONS\COMPLETED_WORKS_MATCHING (BINARY SEARCH + DATE CHECK).py"

"C:\Users\chinjooern\AppData\Local\Continuum\anaconda3\python.exe" "C:\Users\chinjooern\Desktop\TR\ADD-ONS\GENERATE_ALL_TR_WORKS.py"


cmd /k