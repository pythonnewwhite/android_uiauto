import json

class Handle_Json:

    def get_json_value(self,json_data,key):
        if isinstance(json_data,dict):
            for i in json_data.keys():
                if isinstance(json_data[i],dict):
                    return self.get_json_value(json_data[i],key)
                if i ==key:
                    return json_data[i]






if __name__ == '__main__':
        hj=Handle_Json()
        data={'bounds': {'bottom': 2072, 'left': 286, 'right': 329, 'top': 1960}, 'childCount': 0,
         'className': 'android.widget.CheckBox', 'contentDescription': '', 'packageName': 'com.tima.gac.passengercar',
         'resourceName': None, 'text': '', 'visibleBounds': {'bottom': 2072, 'left': 286, 'right': 329, 'top': 1960},
         'checkable': True, 'checked': False, 'clickable': False, 'enabled': True, 'focusable': True, 'focused': False,
         'longClickable': False, 'scrollable': False, 'selected': False}

        value=hj.get_json_value(json_data=data,key='left')
        print(type(value),value)
