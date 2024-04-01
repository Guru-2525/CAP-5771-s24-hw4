# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "No"
    answers["(b)"] = "No"
    answers["(c)"] = "Yes"        
    answers["(d)"] = "Yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "Rules are counting as conflicting if no given case (or instance) satisfies more than one rule together. Unfortunately, within this pool, the overlaps are likely to occur. In this case, a homeowner who satisfies rule (1) could also have downgraded annual income under rule (3) and he could be marked as the defaulted borrower (DB = Yes). This fact however does not make the rules mutually inconclusive because an individual's own attributes could be stimulators of many rules."
    answers["(b) explain"] = "Any rule which does not apply in an situation is called a mutually exclusive rule and, in that situation, a case (instance) cannot satisfy more than one rule. Here it is overlapping with another. Consequently, a Home Owner (H= Yes) might also be a person that has Low Annual Income (L= Yes), which means that the individual would fulfill both conditions that a defaulted borrower (DB = yes) should have. In this case, those rules may not be mutually exclusive as efforts of one individual can be guided by more than one rule."
    answers["(c) explain"] = "Therefore, because the rules are not independent, the order of them could be a factor in the final classification result. If a case falls under more than one rule, the order defines which of the rules takes effect first and therefore impacts the default borrower's final decision response. Ranking the rules ensure the uniformly fair results."
    answers["(d) explain"] = "The rule set is not complete excluding cases that do not conform to the presented rules. The classes are required to classify cases that are unmatched. The default class will be a catch-all classification making sure that all the cases will be possessed by this classification even if they don't fall under the specific rules. Lack of a default class will lead to the fact that some of the individuals will remain unclassified. That is undesirable in a rule-based system where the final purpose is to make the definite predictions."

    return answers


# -----------------------------------------------------------
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "Yes"
    answers["(b)"] = "No"
    answers["(c)"] = "No"
    answers["(d)"] = ""

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "Yes"
    answers["(b)"] = "No"
    answers["(c)"] = "No"

    # explain-string: explanation in english prose
    answers["(a) example"] = "Rules are between pairs of cases when no case can satisfy more than one rules at a time.In this set:R1 will define air-breathing organisms that do not give birth as birds.R2 in this system defines any aquatic vertebrate that is not oviparous to be a fish.R3:Any vertebrate that is warm-blooded is a mammal is defined as R3.R4 designates the reptiles as the animals having live birth, not birds, and not fishes.These rules are mutually exclusive since each rule has a particular combination of attribute values to trigger them that are not common with others"
    answers["(b) example"] = "The rules set will be so extensive that it will combine all possible cases. Each data set entry will be assessed and, at least, one rule will classify all of them. Moreover, these rules do apply only in select cases. Therefore, amphibians and birds are not specifically mentioned by these rules, as none of these rules include vertebrates that are cold-blooded and give birth (the case of the salamander) or warm-blooded, give birth, but are not aerial creatures (for example, the penguin)."
    answers["(c) example"] = "Since they are disjointed, at the most one instance would be applicable to a given context and consequently the order in which they are applied does not matter. The process of classifying will be drained of any randomness because regardless the order, each example will be categorized the same way only that it will be reflective of one of the rules being followed. Nevertheless, it has to be pointed out that the reasons which are not in the list of the reasons may not occur to be categorized at all which is a different issue from where the reasons fit in the rules."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "The gradient at the (k+1)th layer is used to calculate the gradient at the kth layer, by applying the chain rule to get the accurate value, which is the base to update the weights of each layer in the network."
    answers["(b) explain"] = "When an ANN process goes from the kth layer to k+1th, the activation at k+1 is calculated using the weights of the nodes at k and activating them through a summation followed by applying a function."
    answers["(c) explain"] = "In ANN training, the vanishing gradient issue, arises when it becomes hard for the algorithm to propagate gradients through backward layers resulting in no or minor learning at the earlier layers — and this not about backpropagating training errors prompting disappearance."
    answers["(d) explain"] = "Even if ANN performance is perfect, it doesn't mean that gradients of the loss function wrt weights at each layer will be equal to zero. If the model is to be at a global optimal minimum, then the gradient will be zero. On the other hand, a perfect classification of the training set can also be the outcome of model tailored to the specific data and can still have non-zero gradients, because of the fact that loss function often allow for margins of error."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.28
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "No"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.4
    answers["(c) P(X_2=1 | +)"] = 0.4
    answers["(c) P(X_2=1 | -)"] = 0.5
    answers["(c) P(X_3=1 | +)"] = 0.16
    answers["(c) P(X_3=1 | -)"] = 0

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.25

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 1
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "The plot in figure KNN (a) reveals that the clusters are easy to distinguish by the different colors, hereby showing no class overlap. When such kind of case is seen, K with a small value is taken as the most preferable choice because all the instances of each class are closely packed in the space. Actually, at this stage, when K = 1 provides slightly better performance, misjudgment of this type is rather unlikely since there are too few neighbors involved. Since class separation is better than in scenario A, K=50 could be too much for the case and could over smooth the decision boundary which would better be the second choice."
    answers["(b) explain"] = "Figure KNN (b) plotted the more overlapping space between the classes, indicating that each instance of class is not necessarily representative of the overall class distribution due to noise or class overlapping. A big k would be preferred here for that the classifier's conclusion is based on a greater swath of neighbors, which nullifies the sound effect of noise. A good compromise could be K = 5 that prevents a smoother decision boundary from being too sensitive to outliers, as it is for K = 1, while still detailed enough to adapt to complexities of true class boundaries better than K = 50, which might be too smooth and would cause the model to underfit. While in the former case when the decision boundary becomes ambiguous the K = 50 might fail to highlight particular fine details of the data."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.4
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.4
    answers["(a) P(A=1|-)"] = 0.8
    answers["(a) P(B=1|-)"] = 0.0
    answers["(a) P(C=1|-)"] = 0.4

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "1. Calculate the frequency of occurrence when the class is a positive (+) and the attribute is 1.Count down by the number of positive (+) occurrences. Divide counts from step 1 by the counts from step 2 to get \( P(Attribute = 1 | Class = +) \).4. Now, do the same for negative class (-).Count the instances where A=1 and the class is +**: Those can be seen through the table; where instances 5 and 10 have  A=1  and classified as positive.Count the total number of positive instances: Examples 2, 5, 6, 9, and 10 are positive, making that there are 5 positive cases.Calculate \( P(A=1 | +) \)**: Of which there were 2 \( A=1 \) among the 5 positive occasions, \( P(A=1 |+) = \frac{2}{5} \)."

    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0
    answers["(b) P(R|+)"] = 0.064
    answers["(b) P(R|-)"] = 0.0

    # string, '+' or '-'
    answers["(b) class label"] = "+"

    # explain_string
    answers["(b) Explain your reasoning"] = "For a Naive Bayes test case of all features set to 1, the classifier assigns to the positive class. Therefore, the conditional probability for one feature given the negative class would be zero as well, which would make the joint likelihood of the negative class exactly zero. This, therefore, implies the positive class as the only workable prediction."
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.3
    answers["(c) P(A=1,B=1)"] = 0.1

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = "No"
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.7
    answers["(d) P(A=1,B=0)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "No"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.4
    answers["(e) P(A=1|+)"] = 0.8
    answers["(e) P(B=1|+)"] = 0.5

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "Yes"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "As a matter of fact, A and B are conditionally independent, given the class+. That is mainly founded on the necessity for the conditional independence at the time conditional independence constraints vanishes in the framework of the Naive Bayes classifier as per its condition.A and B being conditionally independent under the class if P(A&B/class)=P(A/class) x P(B/class)."
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
