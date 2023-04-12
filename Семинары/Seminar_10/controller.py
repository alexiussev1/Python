import view, model, text_fields as txt

def start_pb():
    while True:
        choise = view.main_menu()
        match choise:
            case 1:
                model.load_file()
                view.print_info(txt.load_success_full)
            case 2:
                model.save_file()
                view.print_info(txt.save_success_full)
            case 3:
                pb= model.get_pb()
                view.show_contacts(pb, txt.no_contact_or_file)
            case 4:
                contact = view.new_contact
                model.add_contact(contact)
                view.print_info(txt.new_contact_success_full)
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                if model.exit_pb():
                    if view.confirm(txt.is_change):
                        model.save_file()
                view.print_info(txt.bay_bay)
                exit()
                
            # case _: если вcе другое не сработало