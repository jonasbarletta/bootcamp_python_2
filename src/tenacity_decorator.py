from tenacity import retry, stop_after_attempt, wait_fixed


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_user_input():

    user_input = input('Digite "ok" para continuar \n')

    if user_input.lower() != "ok":

        print("Input incorreto. Por favor, tente novamente.")
        raise ValueError("Input Incorreto")
    else:
        print("Input correto. Continuando...")


get_user_input()
