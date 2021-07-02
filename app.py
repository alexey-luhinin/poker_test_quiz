from flask import Flask, render_template, request, redirect
from flask.helpers import url_for

from typing import List
from random import shuffle


app = Flask(__name__)


class Question:
    def __init__(self, question: str, answers: List[str], correct_answer: str) -> None:
        self._question = question
        self._answers = answers
        self._correct_answer = correct_answer

    def __str__(self) -> str:
        return self._question

    @property
    def question(self) -> str:
        return self._question

    @property
    def answers(self) -> List[str]:
        return self._answers

    @property
    def correct_answer(self) -> str:
        return self._correct_answer

    def check_answer(self, answer: str) -> bool:
        return self._correct_answer == answer

    def shuffle_answers(self):
        shuffle(self._answers)


class Test:
   def __init__(self, questions: List[Question]) -> None:
        self._questions = questions
        self._list_of_correct = []
        self._list_of_incorrect = []
    

   def __len__(self) -> int:
       return len(self._questions)

   def pop(self) -> Question:
       return self._questions.pop()

   def __getitem__(self, pos: int) -> Question:
       return self._questions[pos]

   def add_to_correct(self, question: Question) -> None:
       self._list_of_correct.append(question)

   def add_to_incorrect(self, question: Question) -> None:
       self._list_of_incorrect.append(question)

   @property
   def list_of_correct(self) -> List[Question]:
       return self._list_of_correct

   @property
   def list_of_incorrect(self) -> List[Question]:
       return self._list_of_incorrect

   def shuffle_answers(self) -> None:
       shuffle(self._questions)

   def reset_test(self) -> None:
       self._questions += self._list_of_correct
       self._questions += self._list_of_incorrect
       self._list_of_correct = []
       self._list_of_incorrect = []


@app.route('/')
def index():
    return render_template('index.html', numbers_of_questions=len(poker_test))


@app.route('/test', methods=['GET', 'POST'])
def test():
    if len(poker_test) == 0:
        correct = len(poker_test.list_of_correct)
        incorrect = len(poker_test.list_of_incorrect)
        poker_test.reset_test()
        return render_template('result.html', correct=correct, incorrect=incorrect)

    if request.method == 'POST':
        answer = request.form['answer']
        q = poker_test.pop()

        if q.check_answer(answer):
            poker_test.add_to_correct(q)
        else:
            poker_test.add_to_incorrect(q)
        return redirect(url_for('test'))

    return render_template('test.html', question=poker_test[-1])


if __name__ == '__main__':
    q1 = Question('BU(hero) vs BB<br /> \
                <img class="card" src="/static/img/8S.png"> \
                <img class="card" src="/static/img/9S.png"> \
                <br />Hero opens 2.5bb, bb call. bb checks, hero?\
                <br />\
                <br />Flop (5.5 bb)<br /> \
                <img class="card" src="/static/img/AH.png"> \
                <img class="card" src="/static/img/7H.png"> \
                <img class="card" src="/static/img/2S.png">', 
                ['CBET 25%', 'CBET 33%', 'CBET 66%', 'CHECK'], 'CBET 66%')

    q2 = Question('BU(hero) vs BB<br /> \
                <img class="card" src="/static/img/3C.png"> \
                <img class="card" src="/static/img/3D.png"> \
                <br />Hero opens 2.5bb, bb call. bb checks, hero?\
                <br />\
                <br />Flop (5.5 bb)<br /> \
                <img class="card" src="/static/img/KH.png"> \
                <img class="card" src="/static/img/8H.png"> \
                <img class="card" src="/static/img/3S.png">', 
                ['CBET 25%', 'CBET 33%', 'CBET 66%', 'CHECK'], 'CBET 66%')

    q3 = Question('BU vs BB(hero)<br /> \
                <img class="card" src="/static/img/8D.png"> \
                <img class="card" src="/static/img/9D.png"> \
                <br />Bu opens 2.5bb, Hero call. Bu cbet 33%, hero?\
                <br />\
                <br />Flop (5.5 bb)<br /> \
                <img class="card" src="/static/img/QC.png"> \
                <img class="card" src="/static/img/JD.png"> \
                <img class="card" src="/static/img/5S.png">', 
                ['XR-B', 'XR-XF', 'XF', 'XC'], 'XC')

    q4 = Question('BU(hero) vs BB<br /> \
                <img class="card" src="/static/img/AC.png"> \
                <img class="card" src="/static/img/10C.png"> \
                <br />Hero opens 2.5bb, bb call. bb checks, hero?\
                <br />\
                <br />Flop (5.5 bb)<br /> \
                <img class="card" src="/static/img/JH.png"> \
                <img class="card" src="/static/img/8H.png"> \
                <img class="card" src="/static/img/2C.png">', 
                ['CBET/FOLD 25%', 'CBET/FOLD 33%', 'CHECK', 'CBET/FOLD 66%', 'CBET/CALL 25%', 'CBET/CALL 33%'], 'CHECK')

    q5 = Question('BU vs BB(hero)<br /> \
                <img class="card" src="/static/img/AC.png"> \
                <img class="card" src="/static/img/7H.png"> \
                <br />Bu opens 2.5bb, hero call. Flop bu cbet 33%, hero call. Turn bu cbet 75%, hero call. River bu cbet 33%, hero?\
                <br />\
                <br />River (22.8 bb)<br /> \
                <img class="card" src="/static/img/AH.png"> \
                <img class="card" src="/static/img/10D.png"> \
                <img class="card" src="/static/img/3H.png"> \
                <img class="card" src="/static/img/6D.png"> \
                <img class="card" src="/static/img/2H.png">', 
                ['X/C', 'X/F', 'X/R'], 'X/F')

    q6 = Question('BU vs BB(hero)<br /> \
                <img class="card" src="/static/img/AC.png"> \
                <img class="card" src="/static/img/7H.png"> \
                <br />Bu opens 2.5bb, hero call. Flop bu cbet 33%, hero call. Turn bu cbet 75%, hero call. River bu cbet 75%, hero?\
                <br />\
                <br />River (22.8 bb)<br /> \
                <img class="card" src="/static/img/AH.png"> \
                <img class="card" src="/static/img/10D.png"> \
                <img class="card" src="/static/img/3H.png"> \
                <img class="card" src="/static/img/6D.png"> \
                <img class="card" src="/static/img/2H.png">', 
                ['X/C', 'X/F', 'X/R'], 'X/C')

    q7 = Question('BU(hero) vs BB<br /> \
                <img class="card" src="/static/img/QC.png"> \
                <img class="card" src="/static/img/JC.png"> \
                <br />Hero opens 2.5bb, bb call. Flop hero cbet 25%, villain call. bb checks, hero?\
                <br />\
                <br />Turn (8.25 bb)<br /> \
                <img class="card" src="/static/img/KH.png"> \
                <img class="card" src="/static/img/KD.png"> \
                <img class="card" src="/static/img/5S.png"> \
                <img class="card" src="/static/img/2C.png">', 
                ['CBET 66%', 'CHECK', 'CBET 125%'], 'CBET 66%')

    q8 = Question('BU(hero) vs BB<br /> \
                <img class="card" src="/static/img/KD.png"> \
                <img class="card" src="/static/img/QS.png"> \
                <br />Hero opens 2.5bb, bb call. bb checks, hero?\
                <br />\
                <br />Flop (5.5 bb)<br /> \
                <img class="card" src="/static/img/AH.png"> \
                <img class="card" src="/static/img/8D.png"> \
                <img class="card" src="/static/img/4D.png">', 
                ['CBET/FOLD 25%', 'CBET/FOLD 33%', 'CHECK', 'CBET/FOLD 66%', 'CBET/CALL 25%', 'CBET/CALL 33%'], 'CBET/FOLD 66%')

    q9 = Question('BU(hero) vs BB<br /> \
                <img class="card" src="/static/img/3C.png"> \
                <img class="card" src="/static/img/3D.png"> \
                <br />Hero opens 2.5bb, bb call. Flop hero cbet 25%, villain call. bb checks, hero?\
                <br />\
                <br />Turn (8.25 bb)<br /> \
                <img class="card" src="/static/img/QH.png"> \
                <img class="card" src="/static/img/QC.png"> \
                <img class="card" src="/static/img/7D.png"> \
                <img class="card" src="/static/img/3S.png">', 
                ['CBET 66%', 'CHECK', 'CBET 125%'], 'CBET 125%')

    q10 = Question('BU vs BB(hero)<br /> \
                <img class="card" src="/static/img/KC.png"> \
                <img class="card" src="/static/img/8D.png"> \
                <br />Bu opens 2.5bb, hero call. Flop bu cbet 33%, hero call. Turn bu cbet 75%, hero call. River bu cbet 95%, hero?\
                <br />\
                <br />River (22.8 bb)<br /> \
                <img class="card" src="/static/img/KH.png"> \
                <img class="card" src="/static/img/10C.png"> \
                <img class="card" src="/static/img/7H.png"> \
                <img class="card" src="/static/img/3C.png"> \
                <img class="card" src="/static/img/5S.png">', 
                ['X/C', 'X/F', 'X/R'], 'X/F')

    q11 = Question('BU vs SB(hero)<br /> \
                <img class="card" src="/static/img/AH.png"> \
                <img class="card" src="/static/img/AC.png"> \
                <br />Bu opens 2.5bb, Hero 3bet, villain call. Hero?\
                <br />\
                <br />Flop (23.5 bb)<br /> \
                <img class="card" src="/static/img/8C.png"> \
                <img class="card" src="/static/img/5D.png"> \
                <img class="card" src="/static/img/3S.png">', 
                ['CBET 33%', 'CBET 50%', 'CHECK'], 'CHECK')

    q12 = Question('BU vs BB(hero)<br /> \
                <img class="card" src="/static/img/QC.png"> \
                <img class="card" src="/static/img/10D.png"> \
                <br />Bu opens 2.5bb, Hero call. Hero?\
                <br />\
                <br />Flop (5.5 bb)<br /> \
                <img class="card" src="/static/img/JH.png"> \
                <img class="card" src="/static/img/9D.png"> \
                <img class="card" src="/static/img/5H.png">', 
                ['XR-B', 'XR-XF', 'XF', 'XC'], 'XR-B')

    q13 = Question('BU(hero) vs BB<br /> \
                <img class="card" src="/static/img/7S.png"> \
                <img class="card" src="/static/img/7H.png"> \
                <br />Hero opens 2.5bb, bb call. bb checks, hero?\
                <br />\
                <br />Flop (5.5 bb)<br /> \
                <img class="card" src="/static/img/JH.png"> \
                <img class="card" src="/static/img/9C.png"> \
                <img class="card" src="/static/img/7D.png">', 
                ['CBET 25%', 'CBET 33%', 'CHECK', 'CBET 50%', 'CBET 66%', 'CBET 75%'], 'CBET 50%')

    q14 = Question('BU vs BB(hero)<br /> \
                <img class="card" src="/static/img/KC.png"> \
                <img class="card" src="/static/img/8H.png"> \
                <br />Bu opens 2.5bb, Hero call. Flop check-check. Hero?\
                <br />\
                <br />Turn (5.5 bb)<br /> \
                <img class="card" src="/static/img/8C.png"> \
                <img class="card" src="/static/img/5D.png"> \
                <img class="card" src="/static/img/2S.png"> \
                <img class="card" src="/static/img/KD.png">', 
                ['XR', 'BET 33%', 'BET 66%', 'BET 125%', 'XC'], 'XR')

    q15 = Question('BU vs BB(hero)<br /> \
                <img class="card" src="/static/img/QC.png"> \
                <img class="card" src="/static/img/8H.png"> \
                <br />Bu opens 2.5bb, Hero call. Flop check-check. Hero?\
                <br />\
                <br />Turn (5.5 bb)<br /> \
                <img class="card" src="/static/img/8C.png"> \
                <img class="card" src="/static/img/5D.png"> \
                <img class="card" src="/static/img/2S.png"> \
                <img class="card" src="/static/img/KD.png">', 
                ['XR', 'BET 33%', 'BET 66%', 'BET 125%', 'XC'], 'BET 33%')

    q16 = Question('BU(hero) vs BB<br /> \
                <img class="card" src="/static/img/5H.png"> \
                <img class="card" src="/static/img/4H.png"> \
                <br />Hero opens 2.5bb, bb call. Flop hero cbet 25%, villain call. bb checks, hero?\
                <br />\
                <br />Turn (8.25 bb)<br /> \
                <img class="card" src="/static/img/JS.png"> \
                <img class="card" src="/static/img/10D.png"> \
                <img class="card" src="/static/img/6C.png"> \
                <img class="card" src="/static/img/3H.png">', 
                ['CBET 75%', 'CHECK', 'CBET 125%'], 'CBET 75%')

    q17 = Question('BU vs SB(hero)<br /> \
                <img class="card" src="/static/img/AS.png"> \
                <img class="card" src="/static/img/4S.png"> \
                <br />Bu opens 2.5bb, Hero 3bet, villain call. Flop hero cbet 50%, villain call. Turn hero cbet 50%, villain call. Hero? \
                <br />\
                <br />River (86 bb)<br /> \
                <img class="card" src="/static/img/2H.png"> \
                <img class="card" src="/static/img/10D.png"> \
                <img class="card" src="/static/img/3D.png"> \
                <img class="card" src="/static/img/3H.png"> \
                <img class="card" src="/static/img/QS.png">', 
                ['ALL-IN', 'X/F'], 'ALL-IN')

    q18 = Question('BU(hero) vs MP<br /> \
                <img class="card" src="/static/img/QS.png"> \
                <img class="card" src="/static/img/JS.png"> \
                <br />Mp opens 2.5bb, Hero 3bet, villain call. Flop Mp check, hero cbet 50%, villain call. Turn Mp check hero cbet 66%, villain call. River Mp check? Hero? \
                <br />\
                <br />River (86 bb)<br /> \
                <img class="card" src="/static/img/9C.png"> \
                <img class="card" src="/static/img/4H.png"> \
                <img class="card" src="/static/img/5C.png"> \
                <img class="card" src="/static/img/3D.png"> \
                <img class="card" src="/static/img/3S.png">', 
                ['ALL-IN', 'CHECK'], 'ALL-IN')

    q19 = Question('CO vs SB(hero)<br /> \
                <img class="card" src="/static/img/JH.png"> \
                <img class="card" src="/static/img/10H.png"> \
                <br />CO opens 2.5bb, Hero 3bet, villain call. Flop hero cbet 50%, villain call. Hero? \
                <br />\
                <br />Turn (43 bb)<br /> \
                <img class="card" src="/static/img/4S.png"> \
                <img class="card" src="/static/img/2H.png"> \
                <img class="card" src="/static/img/6D.png"> \
                <img class="card" src="/static/img/2C.png">', 
                ['BET 66%', 'X/F'], 'BET 66%')

    q20 = Question('BU(hero) vs BB<br /> \
                <img class="card" src="/static/img/QC.png"> \
                <img class="card" src="/static/img/JH.png"> \
                <br />Hero opens 2.5bb, bb call. Flop hero cbet 33%, villain call. bb checks, hero cbet 75%, villain call. bb checks, Hero?<br /><i>villain is a one of the best regs on limit</i>\
                <br />\
                <br />River (22.8 bb)<br /> \
                <img class="card" src="/static/img/8C.png"> \
                <img class="card" src="/static/img/10H.png"> \
                <img class="card" src="/static/img/3S.png"> \
                <img class="card" src="/static/img/7C.png"> \
                <img class="card" src="/static/img/9S.png">', 
                ['CBET 75%', 'ALL-IN', 'CBET 33%'], 'CBET 33%')

    questions = []
    questions.append(q1)
    questions.append(q2)
    questions.append(q3)
    questions.append(q4)
    questions.append(q5)
    questions.append(q6)
    questions.append(q7)
    questions.append(q8)
    questions.append(q9)
    questions.append(q10)
    questions.append(q11)
    questions.append(q12)
    questions.append(q13)
    questions.append(q14)
    questions.append(q15)
    questions.append(q16)
    questions.append(q17)
    questions.append(q18)
    questions.append(q19)
    questions.append(q20)

    for q in questions:
        q.shuffle_answers()

    poker_test = Test(questions)
    poker_test.shuffle_answers()


    app.run(debug=True)