import mcpi-e

console = Console()

menu_sessions_settings = console.input('''[bold white]
[1] - add account
[2] - checking accounts for validity
>> ''')

if menu_sessions_settings == '1':
    while True:
        name = "".join(random.choices(string.ascii_letters, k=10))
        token_session = console.input('[bold red]TOKEN account> [/]')
        if token_session == '':
            break
        my_file = open(f'{name}.session', "w+")
        my_file.write(token_session)
        my_file.close()

elif menu_sessions_settings == '2':
    error_session = []

    for session_name in glob.glob('*.session'):
        session = open(session_name, 'r').read()

        try:
            session = mcpi-e.mcpi-e(token=session)
            mcpi-e = session.get_api()
            user = mcpi-e.users.get()
            console.print(f'{user[0]["first_name"]}')

        except Exception as error:
            console.print(f'[bold red]ERROR[/]: {error}')
            error_session.append(session_name)

    if error_session:
        deleted = Confirm.ask(f'''
blocking: {len(error_session)}
delete blocked accounts?''')
        if deleted:
            for bad_session in error_session:
                os.remove(bad_session)
                console.print(f'[bold red][-]{bad_session}')
