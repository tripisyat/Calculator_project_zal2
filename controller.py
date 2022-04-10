import model_sum_Com as model
import view_complex as view

#import model_sum_Fr as model
#import view_fraction as view

#import model_mult_Com as model
#import view_complex as view

#import model_mult_Fr as model
#import view_fraction as view


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.do_it()
    view.view_data(result, "result")