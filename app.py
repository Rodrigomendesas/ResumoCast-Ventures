from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def get_openai_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a resourceful assistant with an eye for business, skilled in providing creative ideas from varied inputs."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def main():
    questions = [
        "1. Quem você acha que seria uma boa pessoa para te ajudar a ter ideias sobre isso?",
        "2. Quantas sugestões você gostaria de receber?",
        "3. Qual(is) área(s) de atuação você pretende que a sua startup atue?",
        "4. Quais são os principais problemas que você pretende resolver com a atuação da sua startup?",
        "5. Que tipo de inovação e disrupção você pretende trazer com a sua startup?",
        "6. Como você acha que sua startup pode escalar com rapidez?",
        "7. Quais recursos tecnológicos você considera importantes para a sua startup?",
        "8. Qual demanda de mercado você entende que sua startup deve atender?",
        "9. Por fim, qual é o público alvo da sua startup?"
    ]

    answers = []

    print("""
        *** Brainstorming Startups App ***
        Bem-vindo ao nosso gerador de conceitos de startups! Nosso objetivo é fazer algumas perguntas para 
        ajudar você a pensar e criar ideias disruptivas e personalizadas para sua nova empresa. 
        Preencha o formulário abaixo e deixe a inovação começar!
          """)

    for question in questions:
        answer = input(question + "\n> ")
        answers.append(answer)

    prompt = (
        f"Assuma o papel de {answers[0]} para essa tarefa. Eu preciso de conceitos inovadores de startups e para isso preciso que você me dê {answers[1]} sugestões. "
        f"Essa startup deve atuar na área de {answers[2]} e eu pretendo que essa startup resolva os seguintes tipos de problema: {answers[3]}. "
        f"Os principais conceitos de disrupção que eu pretendo ter são {answers[4]}. Além disso, a startup deverá escalar levando em conta {answers[5]}. "
        f"Leve em conta nas suas sugestões que eu pretendo contar com os seguintes recursos tecnológicos: {answers[6]}. "
        f"Por fim, leve em conta também que as principais demandas do mercado que essa startup deve atender são {answers[7]}, "
        f"sendo que meu público-alvo é {answers[8]}."
    )

    response_text = get_openai_response(prompt)

    print("\nSuas respostas:")
    for i, answer in enumerate(answers):
        print(f"{questions[i]} {answer}")

    print("\nResposta gerada pelo OpenAI:\n")
    print(response_text)

if __name__ == '__main__':
    main()
