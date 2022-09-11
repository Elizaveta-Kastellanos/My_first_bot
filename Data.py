import Model_logic
import Logger



def give_Answer(answer):
    Logger.answer_logger(answer)
    Logger.data_logger(answer)
    
def get_data():
    answer = Logger.dive_data_with_log()
    return answer
    



# def give_Answer(answer):
#     return Model_logic.give_me_answer_from_data(answer)


