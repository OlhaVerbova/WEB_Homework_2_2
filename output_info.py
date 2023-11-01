#HomeWork_1

#Abstract class
class ShowInformation():
    def show_all_information(self):
        raise NotImplementedError #required function
    
class Show_to_console(ShowInformation):
    def show_all_information(self, response): 
        print(response)            
    
    def show_error_command(self):
        print("Unknown command. Type 'helper' for a list of available commands.")
    
    def greating_message(self):
        print("Welcome to ContactBot!")
    
    def saved_infornation_addressBook(self, filename, address_book):
        print(f"Address book loaded from {filename}. {len(address_book.data)} contacts found.")