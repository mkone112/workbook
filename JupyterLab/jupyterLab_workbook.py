СМЕНА СТАРТОВОИ ДИРЕКТОРИИ ПРОИСХОДИТ В НАСТРОИКАХ MINTOTRAY

УДАЛЕНИЕ СЕССИИ
    удалить %HOMEPATH%\.ipynb_checkpoints
Built-ins magic commands
	%time
	#тупо замер времени
	
	%timeit

#%%
	начало cell

можно менять тип ячейки
    code
    markdown
    raw
    #if код не пашет -> возм случайно сменил тип
ДОБАВЛЕНИЕ ЯДРА IPYTHON В JUPYTER & ОТДЕЛЬНОГО VENV ВРУЧНУЮ
    #jr сам ставит IPython kernel
    #АЛГ
        activate venv
        #установить ipython kernel
        pip install --user ipykernel
        #|?conda install ipykernel
        #добавление venv в jr
        py -m ipykernel install --user --name=myenv
        >>
            Installed kernelspec myenv in /home/user/.local/share/jupyter/kernels/myenv
        #создает в директории venv kernel.json
        {
            "argv": [
            "/home/urer/anaconda3/envs/myenv/bin/python",
            "-m",
            "ipykernel_launcher",
            "-f",
            "{connection_file}"
            ],
            "display_name": "myenv",
            "language": "pyhton"
        }
УДАЛЕНИЕ VENV ИЗ JUPYTER
    удалить venv
    #видимо из anaconda dir
    jupyter kernelspec
        list
        #>> lst ⊃ available kernels
        #examples
            jupyter kernelspec list
        
        uninstall <venv_name>
        #remove kernel
                

VENVS
    ADD VENVS TO JUPYTER
    