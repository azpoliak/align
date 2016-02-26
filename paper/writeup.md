# Alignment with IBM Model I, Enhanced
Adam Poliak — apoliak1 <br>
Jordan Matelsky — jmatels1

-----

> We intended to implement an alignment algorithm to optimize for reducing AER, basing our work primarily on the IBM Model I<sup id="a1">[1](#f1)</sup>. In the following sections, we explain **(1)** our implementation and **(2)** the specific modifications we made to IBM Model I, and the mathematical motivation behind the modifications.

## Implementation
Our implementation is based on IBM Model I, defining the likelihood of alignment of native word $e$ against foreign word $f$ as:

$\displaystyle P(e|f) =\prod_{i} \sum_{j} P\left( a_i = j  \big{|} |e| \right) $

We experimented with varying numbers of iterations over which to train our model, finally settling on $10$ iterations as a reasonable compromise between accuracy and time-complexity.

## Modifications
In order to improve the accuracy of our alignments, we chose to treat the corpus both as a $e→f$ lookup as well as a $f→e$ lookup. In this way, we were able to train in *two* directions, and then compare the results.

Our initial results took the form of $\left(\left(e_i, f_j\right), P\left(e_i→f_j\right)\right)$, where $e_i$ is a native word, $f_j$ is a foreign word, and $P\left(e_i→f_j\right)$ is the probability that $e_i$ aligns to $f_j$.  With our back-and-forth modification, our results took the form of 2-tuples, where $e_i \in \mathbb{E}, f_j \in \mathbb{F}$:

$$\left[\left(\left(e_i, f_j\right), P\left(e_i→f_j\right)\right), \left(\left(f_j, e_i\right), P\left(f_j→e_i\right)\right)\right]$$

That is, for each $e_i$ and $f_j$, we had either a positive probability of alignment, or no such tuple ($P=0$).

From this point, we chose to experiment with ways of combining the relative probabilities in order to maximize alignment accuracy. Our functions took the form $f : (P(f|e), P(e|f)) → \sigma$, where $\sigma$ was some scalar.

-----
<b id="f1">1</b> Our implementation is derived in general from the text available [here](http://www.statmt.org/book/slides/04-word-based-models.pdf).  [↩](#a1)
