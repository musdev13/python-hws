from django.shortcuts import render

def index(request):
    context = {
        'nickname': 'musdev13',
        'full_name': 'Богдан Андрущак',
        'photo_url': 'https://avatars.githubusercontent.com/u/101466106?v=4',
        'city': 'Винница, Украина',
        'roles': ['Full-Stack Developer', 'Software Engineer', 'DevOps'],
        'email_main': 'sonics0977703996@gmail.com',
        'email_contact': 'cuteemus@gmail.com',
        'phone': '+380 93 093 95 77',
        'phone_plain': '+380930939577',
        'about': 'Full-Stack developer, Software Engineer, DevOps, Femboy и дурачок.',
        'qualities': ['Интроверт', 'Плэйбой', 'Филантроп'],
        'goal': 'Не знаю, скорее всего мидла.',
        'education': {
            'institution': 'КЗ ВЛ №16',
            'specialty': 'Школьник',
            'years': '11-й год обучения',
        },
        'programming_languages': [
            'Rust', 'JavaScript / TypeScript', 'Python',
            'C# (.NET)', 'Java', 'C / C++', 'Lua',
            'Luau (Roblox)', 'Bash',
        ],
        'software': [
            'VS Code', 'Visual Studio', 'Vim / Neovim', 'Arch Linux',
            'Git', 'Docker', 'Photoshop', 'Premiere Pro',
            'After Effects', 'Krita', 'Better Lyrics Composer',
        ],
        'foreign_languages': [
            {'name': 'Русский', 'level': 'основной'},
            {'name': 'English', 'level': 'свободное общение по-теме программирования'},
        ],
        'projects': [
            {
                'title': 'rmlib / rml',
                'subtitle': 'Rust Minecraft Launcher library + CLI',
                'description': (
                    'Модульная Rust-библиотека для работы с Minecraft: '
                    'установка игры, запуск, установка модов и '
                    'ресурспаков. Модульная архитектура через features '
                    'позволяет подключать только нужные части; C ABI-экспорты '
                    'дают возможность собирать библиотеку как .so/.dll и '
                    'использовать из любого языка. rml — CLI-обертка, '
                    'демонстрирующая весь функционал rmlib.'
                ),
                'technologies': [
                    'Rust', 'serde', 'tokio', 'reqwest', 'clap',
                    'zip', 'sha1/sha2', 'crossterm',
                ],
                'result': (
                    'Опубликована версия 0.15.1, репозиторий на GitHub; '
                    'универсальная интегрируемая библиотека для запуска Minecraft.'
                ),
                'link': 'https://github.com/musdev13/rmlib',
            },
            {
                'title': 'LegacyTUI',
                'subtitle': 'C# TUI-обертка над LegacyLauncher',
                'description': (
                    'Терминальный интерфейс для установки и запуска '
                    'Minecraft через LegacyLauncher как отдельных сборок. Имел '
                    'встроенный менеджер модов с поиском и установкой '
                    'с Modrinth.'
                ),
                'technologies': ['C#', 'TUI', 'Modrinth API'],
                'result': (
                    'Предшественник подхода rml/rmlib — после отказа от '
                    'LegacyLauncher как основы проект перерос в собственную '
                    'launcher-библиотеку.'
                ),
                'link': 'https://github.com/musdev13/LegacyTUI',
            },
        ],
    }
    return render(request, 'main/index.html', context)
