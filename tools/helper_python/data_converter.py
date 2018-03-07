# coding=utf-8

def convert_old_data(model):
    try:
        can_be_verified = True
        if 'need_appops' in model.keys():
            if can_be_verified and model['need_appops']:
                can_be_verified = False
            model.pop('need_appops')
        if 'feature_affected' in model.keys():
            if can_be_verified and model['feature_affected']:
                can_be_verified = False
            model.pop('feature_affected')
        if can_be_verified and model['recommended']:
            can_be_verified = False
        model['verified'] = can_be_verified

        if 'reason' in model.keys():
            model['reason']['overwrite_default'] = True
            if ('default' in model['reason'].keys()
                and not 'en' in model['reason'].keys()):
                model['reason']['en'] = model['reason']['default']
                model['reason'].pop('default')
            model['description'] = model['reason']
            model.pop('reason')
        
        return model
    except (RuntimeError, KeyError) as e:
        print('Error when converting data: \'{0}\'\n'.format(model['package']))
        raise(e)
