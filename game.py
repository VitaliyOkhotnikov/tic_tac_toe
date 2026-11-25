from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def save_result(result):
    file = open('results.txt', 'a', encoding='utf-8')
    file.write(result + '\n')
    file.close()


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    # Запускается бесконечный цикл
    while running:
        print(f'Ход делают {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= 3:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= 3:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше  '
                    f'{3}'
                )
                print('Пожалуйста, введите значения для строки и '
                      'столбца заново.'
                      )
                continue
            except CellOccupiedError:
                print('Ячейка занята.')
                print('Введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки '
                      'и столбца заново.'
                      )
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        game.display()

        # После каждого хода надо делать проверку на победу и на ничью
        if game.check_win(current_player):
            result = f'Победили {current_player}.'
            print(result)
            save_result(result)
            running = False
        elif game.is_board_full():
            result = 'Ничья!'
            print(result)
            save_result(result)
            running = False

        current_player = '0' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
