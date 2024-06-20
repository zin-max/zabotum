from aiogram.fsm.state import StatesGroup, State, default_state


# Cоздаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class psy_test(StatesGroup):
    q = State()