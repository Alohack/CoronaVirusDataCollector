from bs4 import BeautifulSoup


class Parser:
    # a static variable
    NUMBER_OF_COUNTRIES = 213
    # Number of parameters except countryName
    NUMBER_OF_PARAMETERS = 13

    # constructor of the parser
    def __init__(self, content):
        # all countries are mt_a class objects
        soup = BeautifulSoup(content, features="html.parser")
        self.mta_objects = soup.findAll("a", {"class": "mt_a"})

    # iterator for the parser
    def __iter__(self):
        for i in range(Parser.NUMBER_OF_COUNTRIES):
            yield self.get_ith_parameters(i)

    # function for removing needless symbols from new parameter
    # like commas and + signs
    @staticmethod
    def remove_needless_symbols_from(thisString):
        return ''.join(x for x in thisString if x != ',' and x != '+' and x != ' ')

    # the function that parses the i-th row for the csv file
    def get_ith_parameters(self, country_index):
        # the object that corresponds to i-th mta class is the i-th country name
        current_tag = self.mta_objects[country_index]

        # the country name is our first parameter
        country_parameters = [current_tag.text]

        # the other parameters are in rows with tag "td"
        # the first td is the parent tag to the current tag
        current_tag = current_tag.parent
        for j in range(Parser.NUMBER_OF_PARAMETERS):
            # finding the next "td" sibling to our tag
            current_tag = current_tag.find_next_sibling("td")

            # We skip this line because it does not contain a parameter
            if j == 5:
                current_tag = current_tag.find_next_sibling("td")

            # The text can contain symbols like commas and + signs
            parameter_with_needless_symbols = str(current_tag.text)

            # removing the commas and + signs (There is no such thing with 12th one which is the mainland)
            if j < 12:
                current_parameter = Parser.remove_needless_symbols_from(parameter_with_needless_symbols)
            # No need to do this for the 12
            else:
                current_parameter = parameter_with_needless_symbols

            # in this website if the value is missing that means it contains 0
            if current_parameter == "\n" or current_parameter == "":
                current_parameter = "0"
            current_parameter = current_parameter;
            # adding the parsed parameter to the end of our parameter list
            country_parameters.append(current_parameter)

        # returning the resulting list
        return country_parameters
