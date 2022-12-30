from Markov import *

#cloud_function(platforms=[Platform.AWS], memory=512, config=config)
def yourFunction(request, context):
    import json
    import logging
    from Inspector import Inspector
    import time
    
    # Import the module and collect data 
    inspector = Inspector()
    inspector.inspectAll()

    # Add custom message and finish the function
    if ('story' in request):
        story = str(request['story'])
        processed_lines = get_processed_lines(story)
        word_list = get_word_list(processed_lines)
        word_str = ' '.join(word_list)
        
        inspector.addAttribute("message", word_str)
    else:
        inspector.addAttribute("message", "ERROR: Improper Input Provided")
    
    inspector.inspectAllDeltas()
    return inspector.finish()
    