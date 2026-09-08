# Day XX — Python Internals, DSA & AI Research

## 🎯 Focus

Today's work focused on strengthening Python internals, solving interview-level DSA problems, and researching how Large Language Models (LLMs) hallucinate and how RAG can reduce hallucinations.

---

## 🐍 Python Internals

### Concepts Covered

* Names, objects and references
* Rebinding vs mutation
* Mutable vs immutable objects
* `id()` and `type()`
* Assignment vs copying
* Shallow copy vs deep copy
* Namespaces and scope
* LEGB rule
* `global` and `nonlocal`
* Function arguments and parameters
* `*args` and `**kwargs`
* Default arguments
* First-class functions
* Closures
* Decorators

### Key Understanding

Python variables are names bound to objects rather than boxes containing values.

Important distinction:

```python
x = [1, 2, 3]
y = x

y.append(4)
```

Both names refer to the same mutable list, so the mutation is visible through both names.

However:

```python
y = [5, 6]
```

rebinds `y` to a new object rather than changing the original list.

### Closures

A closure allows an inner function to remember values from its enclosing function even after the outer function has returned.

```python
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)

print(double(5))
```

### Decorators

A decorator wraps a function and adds behavior without changing the original function's core implementation.

```python
def decorator(func):
    def wrapper(*args):
        print("Starting")
        result = func(*args)
        print("Result:", result)
        return result

    return wrapper
```

---

# 🧠 DSA

## 1. Group Anagrams

### Pattern

Use a dictionary to group words with the same sorted-character representation.

```python
key = ''.join(sorted(word))
```

Example:

```text
eat → aet
tea → aet
ate → aet
```

Therefore they belong to the same group.

### Core Pattern

```python
if key not in groups:
    groups[key] = []

groups[key].append(word)
```

---

## 2. Product of Array Except Self

### Pattern

Use two passes:

1. Left-to-right → calculate products of elements before each position.
2. Right-to-left → multiply by products of elements after each position.

Example:

```text
Input:
[1, 2, 3, 4]

Output:
[24, 12, 8, 6]
```

### Core Idea

```text
left product × right product = answer
```

This avoids division and achieves O(n) time.

---

## 3. Longest Consecutive Sequence

### Pattern

Use a set for O(1)-average lookup.

A number starts a sequence only when:

```python
num - 1 not in num_set
```

Then count forward:

```python
while num + length in num_set:
    length += 1
```

Example:

```text
Input:
[100, 4, 200, 1, 3, 2]

Longest sequence:
1 → 2 → 3 → 4

Answer:
4
```

### Complexity

```text
Time: O(n)
Space: O(n)
```

---

# 🔬 AI Research

## Research Question

### Why do LLMs hallucinate?

An LLM generates responses based on patterns learned during training. It does not automatically verify every generated statement against a reliable external source.

Hallucinations can occur when:

* The model lacks sufficient knowledge about the topic.
* The training information is incomplete or outdated.
* The prompt is ambiguous.
* The model generates a statistically plausible continuation that is not factually correct.
* The model has no direct access to the information required to verify its answer.

### Important Insight

**Confidence does not mean correctness.**

An LLM can produce an answer that sounds highly confident even when the information is incorrect.

---

# 📚 How RAG Reduces Hallucinations

**RAG = Retrieval-Augmented Generation**

Instead of relying only on information encoded in the model, RAG retrieves relevant external information and provides it to the LLM as context before generating an answer.

### Without RAG

```text
Question
   ↓
LLM
   ↓
Answer
```

### With RAG

```text
Question
   ↓
Retrieve relevant documents
   ↓
Retrieved context
   ↓
LLM
   ↓
Grounded answer
```

For example, if a user asks:

> "What is our company's refund policy?"

A RAG system can retrieve the company's current refund-policy document and provide the relevant information to the LLM.

The LLM can then generate its response using that retrieved context.

### Important Limitation

RAG **reduces** hallucinations but does not completely eliminate them.

Hallucinations can still occur if:

* The wrong documents are retrieved.
* The retrieved information is outdated or incorrect.
* The model misunderstands the retrieved context.
* The answer goes beyond the available evidence.

### Research Takeaway

> RAG improves factual grounding by retrieving relevant external information and supplying it to the LLM as context. However, retrieval quality and generation quality both affect the final answer.

---

# 💡 Key Lessons

1. Python variables are references to objects.
2. Mutation and rebinding are different operations.
3. Shallow and deep copies behave differently with nested objects.
4. Python functions are first-class objects.
5. Closures remember values from enclosing scopes.
6. Decorators wrap and extend function behavior.
7. Hash maps and sets are powerful DSA tools.
8. Prefix/suffix thinking can solve array problems efficiently.
9. Recognizing sequence starts can turn a sorting problem into an O(n) solution.
10. LLM confidence does not guarantee factual accuracy.
11. RAG provides external context to improve factual grounding.
12. RAG is not a complete solution to hallucination.

---

# 🚀 Progress

### Technical

* [x] Python internals
* [x] Functions and closures
* [x] Decorators
* [x] DSA practice
* [x] AI research

### Problems Completed

* [x] Group Anagrams
* [x] Product of Array Except Self
* [x] Longest Consecutive Sequence

### Career Systems

* [x] GitHub practice
* [x] LeetCode practice
* [ ] LinkedIn update

---

## Next

Continue building deeper foundations in:

* Python
* DSA
* SQL
* Git/GitHub
* Linux
* Mathematics
* AI/ML
* AI Engineering
* Research
* Projects
* Career preparation
