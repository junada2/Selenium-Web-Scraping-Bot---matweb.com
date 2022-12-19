from material_research.material_research import Research

try:
    with Research() as bot:
        bot.acessar_pag()
        bot.search_type()
        bot.property_type()
        bot.property_value()
        bot.search()
        bot.get_materials_attributes() 

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'Você está tentando rodar o robô em uma linha de comando \n'
            'Por favor adicione o Selenium Driver ao PATH \n'
            'Windows: \n'
            '   set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '   PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise















