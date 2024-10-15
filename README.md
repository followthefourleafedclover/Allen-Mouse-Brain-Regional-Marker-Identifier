# Allen Mouse Regional Marker Identifier
Find region specific markers within the Allen Institute for Brain Science: Mouse Whole Cortex and Hippocampus 10x Dataset

\documentclass{article}
\usepackage{graphicx} % Required for inserting images

\title{Allen Brain: Region Specific Marker Finder Technical Paper}
\author{Sreevar Patiyara}
\date{October 2024}

\begin{document}

\maketitle

\section{Introduction}

Let T be the number of cell types; T \textbf{=} 387.

\vspace{0.5em}
\noindent Let N be the number of genes; N \textbf{=} 29,277.

\vspace{0.5em}
\noindent Let P denote a population of cells C of various types t, such that \( 1 < t \leq T \).

\vspace{0.5em}
\noindent Let R\textsubscript{n} denote an arbitrary subset of P, such that \( R\textsubscript{n} \subseteq P \).

\vspace{0.5em}
\noindent Let G\textsubscript{n} be a gene that may or may not be expressed in the population of cells, such that \( 1 < n \leq N \).

\vspace{0.5em}
\noindent Let C\textsubscript{t}(G\textsubscript{n}) be the expression of the gene \( G\textsubscript{n} \) in the cell type \( C\textsubscript{t} \).

\vspace{1em}
\noindent The mean expression of gene \textit{G} across all cell types is given by:
\[
\mu\textsubscript{G} = \frac{\sum_{i=1}^{T} C\textsubscript{i}(G)}{T}
\]

\noindent The standard deviation of the expression of gene \textit{G} is:
\[
\sigma\textsubscript{G} = \sqrt{\frac{\sum_{i=1}^{T} (C\textsubscript{i}(G) - \mu\textsubscript{G})^2}{T}}
\]

\noindent The z-score of the expression of gene \textit{G} in a cell type \textit{t} is:
\[
\ z\textsubscript{G, t}=\frac{C\textsubscript{t}(G) - \mu\textsubscript{G}}{\sigma\textsubscript{G}}
\]

\noindent The distribution of z-scores or the relative expression of \textit{G} in all cell types is given by:
\[
\ E\textsubscript{G} = \{ z\textsubscript{G,1}\hspace{4pt} ... \hspace{4pt}z\textsubscript{G,387}\}
\]
\vspace{3pt}
\noindent In order to find statically significant values within our relative expression distribution, we need to preform a Mann-Whitney U Test, opposed to a T-test, because our distribution is not normal. 
\[
\ 
\]


\end{document}
