#Коментарии по CLI: 1. Формат CLI выглядит как:
# название_скрипта --- есть
# папка_с_данными_для_обучения --- есть
# список_параметров_из_первичного_датасета --- есть, отредактировано
# расположение_файла_для_рекомендационной_системы --- есть, отредактировано
# расположение_конечного_файла_выгруженных_данных" --- есть
## шаг_дискредитации --- есть
## дискретные_параметры --- есть
## способ_усреднения --- есть

import click
import pandas as pd

list_param = str('Дата и Время, Глубина, Вес на крюке, Высота крюка, Скорость СПО, Нагрузка на долото, Момент на роторе, Глубина долота, Обороты, Давление, Мех.скорость средняя, Ходы насоса 1, Ходы насоса 2, Расход вх., Темп.вх, Темп.вых, Плотность вх., Плотность вых., Поток на вых., Рабочая емк.1, Рабочая емк.2, БПР 1, БПР 2, Долив, ЦСГО, ЦСГО 2, Сумм. актив ёмк., С1, С2, С3, iC4, nC4, iC5, nC5, Сумм.газ.хромат')
d_param = str('Обороты, Ходы насоса 1, Ходы насоса 2')


@click.command()

@click.option(
    "--da",
    "-da",
    "data",
    required=True,
    help="Папка с данными для обучения",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True),
)

@click.option(
    "--p",
    "-p",
    "param",
    default=list_param,
    help="Список параметров:"+list_param,
    type=click.STRING,
)

@click.option(
    "--dp",
    "-dp",
    "d_param",
    default=d_param,
    help="Дискретные параметры"+d_param,
    type=click.STRING,
)

@click.option(
    "--s",
    "-s",
    "step",
    required=True,
    help="Шаг дискредитации",
    type=click.Path(exists=True, file_okay=False, dir_okay=False, readable=False),
)

@click.option(
    "--m",
    "-m",
    "aver_method",
    required=True,
    help="Способ усреднения",
    type=click.Path(exists=True, file_okay=False, dir_okay=False, readable=False),
)

@click.option(
    "--in",
    "-i",
    "in_file",
    required=True,
    help="Расположение_файла_для_рекомендационной_системы",
    type=click.Path(exists=True, dir_okay=False, readable=True),
)

@click.option(
    "--out-file",
    "-o",
    default="./output.xlsx",
    help="Путь к файлу excel для сохранения результата.",
    type=click.Path(dir_okay=False),
)

def process(in_file, out_file, data, param, d_param, step, aver_method):

    input = pd.read_excel(in_file)
    output = pd.DataFrame(input)
    write_excel = output.to_excel(out_file)
if __name__ == "__main__":
    process()


