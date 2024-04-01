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
    answers["(a) explain"] = "When it's impossible for a situation to meet more than one set of guidelines, those guidelines are seen as conflicting. However, overlaps in rules can occur. For example, a homeowner who meets the criteria for one rule but not another might still be considered in default. These overlaps show that individual circumstances can trigger multiple rules, suggesting that the rules are not inherently contradictory."
    answers["(b) explain"] = "A rule is mutually exclusive when it doesn't apply in specific situations, preventing a case from satisfying multiple rules simultaneously. However, these rules can conflict with each other. For example, a homeowner (H = Yes) might also meet criteria for low annual income (L = Yes), qualifying them as a defaulted borrower (DB = Yes). In such cases, the rules may not be mutually exclusive because a person's status can be influenced by multiple rules at once."
    answers["(c) explain"] = "The order of rules applied in a decision tree affects the final classification of a borrower's default status. If a situation can be classified under multiple rules, the sequence determines which rule has higher priority and will be used for the classification. This ranking of rules ensures consistent and fair results."
    answers["(d) explain"] = "The rule system is lacking because it doesn't account for when given rules are violated. To categorize cases that don't fit, different categories are needed. The default category covers all cases, even those that don't match specific rules. In a rule-based system designed to make clear predictions, it's not ideal for cases to remain unclassified without a default category."
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
    answers["(a) example"] = "In order to prevent a case from satisfying more than one rule at once, rules are applied between pairs of cases. Within this particular set: R1 describes species that breathe air but do not give birth like birds. According to R2, a fish is any aquatic animal that is not oviparous. According to R3, a mammal is any warm-blooded vertebrate. Reptiles are defined by R4 as living things that are not fish or birds and can give birth to live offspring. Because each rule only triggers certain combinations of attribute values that do not overlap with other rules, they are mutually exclusive."
    answers["(b) example"] = "The rules are designed to apply to all possible situations. Every data entry will be reviewed, and each one will be categorized by at least one rule. However, these rules have limitations. Specifically, animals that are warm-blooded, give birth, and are not aerial (like penguins) or cold-blooded and give birth (like salamanders) are not included in these rules, and therefore neither amphibians nor birds are covered."
    answers["(c) example"] = "Each rule in the set is self-contained, making the order in which the rules are applied irrelevant as only one rule will apply to a given situation. This eliminates any ambiguity in classifying samples, as each sample will be assigned to a class based on a single rule, regardless of the order of application. However, reasons that are not included in the set of rules may remain unclassified, unlike cases where reasons adhere to the defined rules."
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
    answers["(a) explain"] = "By applying the chain rule, we can calculate the precise gradient at the kth layer based on the gradient at the (k+1)th layer. This process serves as the basis for modifying the weights at each layer of the neural network."
    answers["(b) explain"] = "In an artificial neural network, the activation (output) of the (k+1)th layer is determined by: * Multiplying the weights of the nodes in the kth layer by the activation of those nodes * Summing up the multiplication results * Applying an activation function to the sum"
    answers["(c) explain"] = "During the training of an Artificial Neural Network (ANN), the problem of vanishing gradients occurs when the algorithm has difficulty transmitting gradients through previous layers. This leads to minimal or no learning in those layers. It's important to note that this issue is unrelated to the vanishing gradient problem encountered in backpropagation, where training errors are propagated backward through the network."
    answers["(d) explain"] = "Even if an artificial neural network (ANN) performs perfectly on the training set, it doesn't guarantee that the gradients of the loss function with respect to the weights in each layer will be zero. The gradients will only be zero if the model reaches a global optimal minimum. However, since the loss function often tolerates some error, even models that achieve perfect classification on the training set might still have non-zero gradients."
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
    answers["(a) explain"] = "In Figure KNN(a), the classes are well-separated, forming distinct clusters. Because the instances within each cluster are concentrated, using a small value for K (e.g., 1) is preferred. With fewer neighbors, the likelihood of misclassification is reduced. However, while K=1 generally yields better performance in such situations, the small number of neighbors may limit the accuracy. For this particular scenario, with its clear class separation, choosing K=50 as an alternative option might smooth out the decision boundary excessively."
    answers["(a) explain"] = "In KNN (b), when classes overlap or have background noise, individual class points may not fully reflect the class distribution. This is shown by the increased overlap between classes in the plot. In such cases, a larger value of K is preferred to reduce the impact of noise. This is because the classifier's decision is based on a wider range of neighbors. A balanced choice for K is 5. This prevents the classifier from being too sensitive to outliers (like K = 1) while retaining enough detail to follow the boundaries of real classes better than K = 50, which could lead to underfitting. However, if the class boundaries become less clear, a larger value of K (such as K = 50) may be necessary."
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
    answers["(a) P(A=1|+) explain your answer"] = "1. Count the number of instances where the attribute is 1 and the class is positive (+). 2. Subtract this count from the total number of positive instances. 3. Divide the count from step 1 by the count from step 2 to obtain \( P(Attribute = 1 | Class = +) \). **Step 2:** Repeat step 1 for the negative class (-): 1. Count the number of instances where the attribute is 1 and the class is negative (-). 2. Subtract this count from the total number of negative instances. 3. Divide the count from step 1 by the count from step 2 to obtain \( P(A=1 | -) \). In the example provided, for \( P(A=1 | +) \), there are 2 positive instances with \( A=1 \) out of a total of 5 positive instances, resulting in \( P(A=1 | +) = \frac{2}{5}\)."
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0
    answers["(b) P(R|+)"] = 0.064
    answers["(b) P(R|-)"] = 0.0

    # string, '+' or '-'
    answers["(b) class label"] = "+"

    # explain_string
    answers["(b) Explain your reasoning"] = "In a Naive Bayes model, when all feature values are 1, the classifier automatically classifies the instance as positive. Consequently, the probability of the negative class being exactly 0 becomes 0, which in turn makes the conditional probability of any individual feature given the negative class also 0. Since the probability of the negative class is 0, the positive class becomes the only logical prediction."
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
