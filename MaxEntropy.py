from nltk.classify import MaxentClassifier

train = [];

test1 = {'outlook': 'sunny', 'temperature': 'hot', 'humidity': 'high', 'windy': 'FALSE'};
test2 = {'outlook': 'overcast', 'temperature': 'hot', 'humidity': 'high', 'windy': 'FALSE'};
test3 = {'outlook': 'sunny', 'temperature': 'cool', 'humidity': 'high', 'windy': 'TRUE'};
test = [];
test.append(test1);
test.append(test2);
test.append(test3);

def load_data(filename):
    for line in open(filename, mode='r'):
        sample = line.strip().split("\t");
        y = sample[0];
        reason1={'outlook':sample[1],'temperature':sample[2],'humidity':sample[3],'windy':sample[4]};
        if(y=='no'):
            train.append((reason1,'x'));
        elif(y=='yes'):
            train.append((reason1,'y')) ;
def print_maxent_test_header():
    print(' '*11+''.join(['      test[%s]  ' % i
                           for i in range(len(test))]))
    print(' '*11+'     p(x)  p(y)'*len(test))
    print('-'*(11+15*len(test)))
def test_maxent(algorithm):
    print('%11s' % algorithm)
    try:
        classifier = MaxentClassifier.train(
                         train, algorithm, trace=0, max_iter=1000)
    except Exception as e:
        print('Error: %r' % e)
        return

    for featureset in test:
        pdist = classifier.prob_classify(featureset)
        print('%8.15f %6.15f' % (pdist.prob('x'),  pdist.prob('y')))
    print()
if __name__ == '__main__' :
    load_data('data.txt');
    print_maxent_test_header();
    test_maxent('GIS');
    test_maxent('IIS');