import os


def replace_all_occurrences(file_name):
    with open("ose/" + file_name, 'r') as file_input, open("rpl-" + file_name, 'w') as file_output:
        for line in file_input:
            line = line.replace('$(application_name}', appname) \
                .replace('$(environment}', environment)

            if file_name == 'configmap-app.yml':
                if line.strip() == 'filename:':
                    line = line.replace('filename', 'data')
                    file_output.write(line)
                    for line2 in file_input:
                        # line = file_input.readline()
                        properties = line2.split(' - ')
                        file_map = properties[1].strip()
                        file_output.write("\t" + file_map + ": |-\n")
                        with open("resources/" + properties[1].strip(), "r") as new_file:
                            for new_line in new_file:
                                file_output.write("\t\t" + new_line)
                else:
                    file_output.write(line)
            else:
                file_output.write(line)

    file_output.close()


if __name__ == '__main__':

    appname = os.getenv('application_name')
    environment = os.getenv('env')

    with open('files.txt', 'r') as f:
        for yml in f:
            print(yml)
            replace_all_occurrences(yml.rstrip())
