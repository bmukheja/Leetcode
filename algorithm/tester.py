import sys
import json

if __name__ == "__main__":
    problem = sys.argv[1]
    print("Running code of problem {0}".format(problem))
    module_name = 'p{0}'.format(problem)
    with open('{0}_input.json'.format(module_name.split("_")[0]),'r') as input_json:
        inputs = json.load(input_json)
    with open('{0}_output.json'.format(module_name.split("_")[0]),'r') as output_json:
        outputs = json.load(output_json)
    if len(inputs) != len(outputs):
        print("No. of inputs != No. of outputs. {0} vs {1}".format(len(inputs),len(outputs)))
        exit(1)

    sol = __import__(module_name)
    methods = [m for m,n in sol.Solution.__dict__.items() if not m.startswith('__') and not m.startswith('_')]
    if len(methods)>1:
        print("Many public methods defined in the class, reduce it to 1.")
        print methods
        exit(1)
    method = methods[0]
    print("Calling method {0}()\n~~~~~~~~~~~~~~~~~~~~~~~~~~".format(method))
    func = getattr(sol.Solution(),method)
    for i in range(len(inputs)):
        output = func(inputs[i])
        print("Example {0}:\nInput: {1}\nOutput: {2}\nExpected Output: {3}\n".format(i+1,inputs[i],output,outputs[i]))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")