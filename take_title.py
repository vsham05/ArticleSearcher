from main_parser import get_title_and_common_words
import json 





if __name__ == '__main__':
    r = []
    with open('energy_states.txt', 'r') as file:
        data = list(map(lambda x: x.replace('\n', ''),file.readlines()))

    with open('pointer.txt', 'r') as file:
        k = int(file.read())

    with open('states.csv', 'r', encoding='utf-8') as file:
        states = list(map(lambda x: x.replace('\n', ''),file.readlines()))
    
    r = [] + states

    while k < len(data):
        try:
            link = data[k]
            title, d = get_title_and_common_words(link)
            res = [title, link, d]
            print(title)
            r.append(','.join(res))
        except Exception as e:

            print(data[k])
            with open('states.csv', 'w', encoding="utf-8") as writer:
                writer.write('\n'.join(r))

            k += 1
            with open('pointer.txt', 'w') as writer:
                writer.write(str(k))
            break
        
        k += 1

