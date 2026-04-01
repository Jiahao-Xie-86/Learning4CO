# Learning4CO

**Learning for combinatorial optimization** — a personal curated reading list that maps **neural and learning-based methods** (organized by problem) together with a front section on **LLMs and agents for CO**, so you can explore both research threads in one place.

### At a glance

<div align="center">

<img src="https://readme-typing-svg.demolab.com/?lines=Learning4CO;583+papers+indexed;141+tagged+for+LLM+for+CO;20+in+survey+section;36+problem+categories;239+with+code+repo&font=Inter&weight=600&size=24&duration=2600&pause=1000&color=312E81&background=transparent&center=true&vCenter=true&width=680&height=50&repeat=true" alt="Learning4CO" />

<p dir="auto">
  <img src="https://img.shields.io/static/v1?label=Papers&message=583&color=4f46e5&style=flat-square&logo=bookstack&logoColor=white" alt="Papers: 583" />
  <img src="https://img.shields.io/static/v1?label=LLM%20for%20CO&message=141&color=7c3aed&style=flat-square&logo=openai&logoColor=white" alt="LLM for CO: 141" />
  <img src="https://img.shields.io/static/v1?label=Surveys&message=20&color=0e7490&style=flat-square&logo=readthedocs&logoColor=white" alt="Surveys: 20" />
  <img src="https://img.shields.io/static/v1?label=Categories&message=36&color=475569&style=flat-square" alt="Categories: 36" />
  <img src="https://img.shields.io/static/v1?label=With%20code&message=239&color=059669&style=flat-square&logo=github&logoColor=white" alt="With code: 239" />
</p>

</div>

---

## [Content](#content)

### Navigate

<table>
<thead>
<tr><th align="left">Three tracks — pick where to start</th></tr>
</thead>
<tbody>
<tr><td valign="top"><a href="#llm-for-combinatorial-optimization"><strong>① LLM for CO</strong></a><br />
LLMs, agents &amp; tool use for combinatorial optimization</td></tr>
<tr><td valign="top"><a href="#survey-papers"><strong>② Surveys</strong></a><br />
Broad reviews &amp; methodology surveys</td></tr>
<tr><td valign="top"><a href="#problems"><strong>③ Problems</strong></a><br />
Papers by <strong>problem type</strong> (TSP, MIP, SAT, …)</td></tr>
</tbody>
</table>

---

#### Problem categories

<table>
<thead>
<tr><th colspan="2" align="center">Quick links by domain</th></tr>
</thead>
<tbody>
<tr>
	<td>&emsp;<a href=#job-shop-scheduling-problem>3.1 Job Shop Scheduling Problem (JSSP)</a></td>
	<td>&emsp;<a href=#flow-shop-problem>3.2 Flow Shop Problem (FSP)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#sorting-&-ranking>3.3 Sorting & Ranking (Sort&Rank)</a></td>
	<td>&emsp;<a href=#graph-matching>3.4 Graph Matching (GM)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#quadratic-assignment-problem>3.5 Quadratic Assignment Problem (QAP)</a></td>
	<td>&emsp;<a href=#travelling-salesman-problem>3.6 Travelling Salesman Problem (TSP)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#portfolio-optimization>3.7 Portfolio Optimization (PortOpt)</a></td>
	<td>&emsp;<a href=#maximal-cut>3.8 Maximal Cut</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#vehicle-routing-problem>3.9 Vehicle Routing Problem (VRP)</a></td>
	<td>&emsp;<a href=#maximum-independent-set>3.10 Maximum Independent Set</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#generalization>3.11 Generalization</a></td>
	<td>&emsp;<a href=#orienteering-problem>3.12 Orienteering Problem (OP)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#knapsack>3.13 Knapsack</a></td>
	<td>&emsp;<a href=#boolean-satisfiability>3.14 Boolean Satisfiability (SAT)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#computing-resource-allocation>3.15 Computing Resource Allocation</a></td>
	<td>&emsp;<a href=#bin-packing-problem>3.16 Bin Packing Problem (BPP)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#graph-edit-distance>3.17 Graph Edit Distance (GED)</a></td>
	<td>&emsp;<a href=#hamiltonian-cycle-problem>3.18 Hamiltonian Cycle Problem (HCP)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#graph-coloring>3.19 Graph Coloring</a></td>
	<td>&emsp;<a href=#maximal-common-subgraph>3.20 Maximal Common Subgraph (MCS)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#influence-maximization>3.21 Influence Maximization</a></td>
	<td>&emsp;<a href=#max-clique>3.22 Max Clique</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#mixed-integer-programming>3.23 Mixed Integer Programming (MIP)</a></td>
	<td>&emsp;<a href=#causal-discovery>3.24 Causal Discovery</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#game-theoretic-semantics>3.25 Game Theoretic Semantics</a></td>
	<td>&emsp;<a href=#differentiable-optimization>3.26 Differentiable Optimization</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#car-dispatch>3.27 Car Dispatch</a></td>
	<td>&emsp;<a href=#electronic-design-automation>3.28 Electronic Design Automation (EDA)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#conjunctive-query-containment>3.29 Conjunctive Query Containment</a></td>
	<td>&emsp;<a href=#virtual-network-embedding>3.30 Virtual Network Embedding (VNE)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#predict+optimize>3.31 Predict+Optimize</a></td>
	<td>&emsp;<a href=#optimal-power-flow>3.32 Optimal Power Flow</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#facility-location-problem>3.33 Facility Location Problem (FLP)</a></td>
	<td>&emsp;<a href=#combinatorial-drug-recommendation>3.34 Combinatorial Drug Recommendation</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#stochastic-combinatorial-optimization>3.35 Stochastic Combinatorial Optimization</a></td>
	<td>&emsp;<a href=#vertex-cover>3.36 Vertex Cover</a></td>
</tr>
</tbody>
</table>

---

### [LLM for Combinatorial Optimization](#content) · *141 papers*

Papers on **LLM for combinatorial optimization** — work where large language models (or closely related agents and tool use) are central to CO.

1. **ViTSP: A Vision Language Models Guided Framework for Solving Large-Scale Traveling Salesman Problems** ICLR, 2026. [paper](https://arxiv.org/abs/2509.23465), [code](https://github.itap.purdue.edu/uSMART/ViTSP_ICLR2026)
    *Zhuoli Yin, Yi Ding, Reem Khir, Hua Cai*

2. **Rethinking LLM-Driven Heuristic Design: Generating Efficient and Specialized Solvers via Dynamics-Aware Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.20868)

3. **Refining Hybrid Genetic Search for CVRP via Reinforcement Learning-Finetuned LLM** ICLR, 2026. [paper](https://arxiv.org/abs/2510.11121), [code](https://github.com/zaodushi/RFTHGS)
    *Rongjie Zhu, Cong Zhang, Zhiguang Cao*

4. **Reasoning in a Combinatorial and Constrained World: Benchmarking LLMs on Natural-Language Combinatorial Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.02188)

5. **PathWise: Planning through World Model for Automated Heuristic Design via Self-Evolving LLMs** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.20539)

6. **OR-Agent: Bridging Evolutionary Search and Structured Research for Automated Algorithm Discovery** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.13869), [code](https://github.com/qiliuchn/OR-Agent)

7. **LLM-Assisted Automatic Dispatching Rule Design for Dynamic Flexible Assembly Flow Shop Scheduling** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.15738)

8. **LLaMEA-SAGE: Guiding Automated Algorithm Design with Structural Feedback from Explainable AI** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.21511)

9. **Heuristic Search as Language-Guided Program Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.16038)

10. **HeuriGym: An Agentic Benchmark for LLM-Crafted Heuristics in Combinatorial Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2506.07972), [code](https://github.com/cornell-zhang/heurigym)
    *Hongzheng Chen, Yingheng Wang, Yaohui Cai, Hins Hu, Jiajie Li, Shirley Huang, Chenhui Deng, Rongjian Liang, Shufeng Kong, Haoxing Ren, Samitha Samaranayake, Carla P. Gomes, Zhiru Zhang*

11. **Hard Constraints Meet Soft Generation: Guaranteed Feasibility for LLM-based Combinatorial Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.01090)

12. **Generalizable Heuristic Generation Through LLMs with Meta-Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2505.20881), [code](https://github.com/yiding-s/MoH)
    *Yiding Shi, Jianan Zhou, Wen Song, Jieyi Bi, Yaoxin Wu, Zhiguang Cao, Jie Zhang*

13. **Game-Theoretic Co-Evolution for LLM-Based Heuristic Discovery** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.22896)

14. **G-LNS: Generative Large Neighborhood Search for LLM-Based Automatic Heuristic Design** Arxiv, 2026. [paper](https://arxiv.org/abs/2602.08253), [code](https://github.com/ZBoyn/G-LNS)
    *Baoyun Zhao, He Wang, Liang Zeng*

15. **From Heuristic Selection to Automated Algorithm Design: LLMs Benefit from Strong Priors** Arxiv, 2026. [paper](https://arxiv.org/pdf/2603.02792), [code](https://github.com/BaronH07/BAG)

16. **EvoX: Meta-Evolution for Automated Discovery** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.23413), [code](https://github.com/skydiscover-ai/skydiscover)

17. **Evolving Interdependent Operators with Large Language Models for Multi-Objective Combinatorial Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.17899)

18. **EoH-S: Evolution of Heuristic Set using LLMs for Automated Heuristic Design** AAAI, 2026. [paper](https://arxiv.org/abs/2508.03082), [code](https://github.com/FeiLiu36/EoH-S)
    *Fei Liu, Yilu Liu, Qingfu Zhang, Xialiang Tong, Mingxuan Yuan*

19. **Enhancing CVRP Solver through LLM-driven Automatic Heuristic Design** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.23092)

20. **DyACE: Dynamic Algorithm Co-evolution for Online Automated Heuristic Design with Large Language Model** Arxiv, 2026. [paper](https://arxiv.org/pdf/2603.13344)

21. **DSevolve: Enabling Real-Time Adaptive Scheduling on Dynamic Shop Floor with LLM-Evolved Heuristic Portfolios** Arxiv, 2026. [paper](https://arxiv.org/pdf/2603.27628)

22. **DRAGON: LLM-Driven Decomposition and Reconstruction Agents for Large-Scale Combinatorial Optimization** AAMAS, 2026. [paper](https://arxiv.org/abs/2601.06502)
    *Shengkai Chen, Zhiguang Cao, Jianan Zhou, Yaoxin Wu, Senthilnath Jayavelu, Zhuoyi Lin, Xiaoli Li, Shili Xiang*

23. **ConstraintBench: Benchmarking LLM Constraint Reasoning on Direct Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.22465)

24. **CDEoH: Category-Driven Automatic Algorithm Design With Large Language Models** Arxiv, 2026. [paper](https://arxiv.org/pdf/2603.19284)

25. **Bridging Synthetic and Real Routing Problems via LLM-Guided Instance Generation and Progressive Adaptation** AAAI, 2026. [paper](https://arxiv.org/abs/2511.10233), [code](https://github.com/HenryZhu1029/EvoReal)
    *Jianghan Zhu, Yaoxin Wu, Zhuoyi Lin, Zhengyuan Zhang, Haiyan Yin, Zhiguang Cao, Senthilnath Jayavelu, Xiaoli Li*

26. **Beyond the Node: Clade-level Selection for Efficient MCTS in Automatic Heuristic Design** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.00549)

27. **AVO: Agentic Variation Operators for Autonomous Evolutionary Search** Arxiv, 2026. [paper](https://arxiv.org/pdf/2603.24517)

28. **An Agentic Framework with LLMs for Solving Complex Vehicle Routing Problems** ICLR, 2026. [paper](https://openreview.net/forum?id=BMOgYw4EhQ), [code](https://github.com/ZHANG-NI/AFL)
    *Ni Zhang, Zhiguang Cao, Jianan Zhou, Cong Zhang, Yew-Soon Ong*

29. **Algorithmic Prompt-Augmentation for Efficient LLM-Based Heuristic Design for A* Search** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.19622), [code](https://github.com/tb-git-tud/a-ceoh-evolution-of-heuristics)

30. **AdaEvolve: Adaptive LLM Driven Zeroth-Order Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.20133), [code](https://github.com/skydiscover-ai/skydiscover)

31. **X-evolve: Solution space evolution powered by large language models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2508.07932)

32. **VRPAgent: LLM-Driven Discovery of Heuristic Operators for Vehicle Routing Problems** Arxiv, 2025. [paper](https://arxiv.org/pdf/2510.07073), [code](https://github.com/ai4co/vrpagent)

33. **ThetaEvolve: Test-time Learning on Open Problems** Arxiv, 2025. [paper](https://arxiv.org/abs/2511.23473)

34. **Text2Zinc: A Cross-Domain Dataset for Modeling Optimization and Satisfaction Problems in MiniZinc** Arxiv, 2025. [paper](https://arxiv.org/pdf/2503.10642), [code](https://huggingface.co/datasets/skadio/text2zinc)

35. **STRCMP: Integrating Graph Structural Priors with Language Models for Combinatorial Optimization** NeurIPS, 2025. [paper](https://arxiv.org/pdf/2506.11057)

36. **StepORLM: A Self-Evolving Framework With Generative Process Supervision For Operations Research Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.22558)

37. **Solver-Informed RL: Grounding Large Language Models for Authentic Optimization Modeling** NeurIPS, 2025. [paper](https://arxiv.org/pdf/2505.11792), [code](https://github.com/Cardinal-Operations/SIRL)

38. **ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution** ICLR, 2025. [paper](https://arxiv.org/pdf/2509.19349), [code](https://github.com/SakanaAI/ShinkaEvolve)

39. **RoCo: Role-Based LLMs Collaboration for Automatic Heuristic Design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.03762)

40. **REMoH: A Reflective Evolution of Multi-objective Heuristics approach via Large Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.07759)

41. **ReflecSched: Solving Dynamic Flexible Job-Shop Scheduling via LLM-Powered Hierarchical Reflection** Arxiv, 2025. [paper](https://arxiv.org/pdf/2508.01724)

42. **RedAHD: Reduction-Based End-to-End Automatic Heuristic Design with Large Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2505.20242)

43. **Planning of Heuristics: Strategic Planning on Large Language Models with Monte Carlo Tree Search for Automating Heuristic Optimization** Arxiv, 2025. [paper](https://arxiv.org/pdf/2502.11422)

44. **Pareto-Grid-Guided Large Language Models for Fast and High-Quality Heuristics Design in Multi-Objective Combinatorial Optimization** AAAI, 2025. [paper](https://arxiv.org/pdf/2507.20923), [code](https://github.com/langkhachhoha/MPaGE)

45. **ORMind: A Cognitive-Inspired End-to-End Reasoning Framework for Operations Research** ACL, 2025. [paper](https://arxiv.org/pdf/2506.01326), [code](https://github.com/XiaoAI1989/ORMind)

46. **OR-LLM-Agent: Automating Modeling and Solving of Operations Research Optimization Problem with Reasoning Large Language Model** Arxiv, 2025. [paper](https://arxiv.org/pdf/2503.10009), [code](https://github.com/bwz96sco/or_llm_agent)

47. **OptiTree: Hierarchical Thoughts Generation with Tree Search for LLM Optimization Modeling** NeurIPS, 2025. [paper](https://arxiv.org/pdf/2510.22192), [code](https://github.com/MIRALab-USTC/OptiTree)

48. **OptiMind: Teaching LLMs to Think Like Optimization Experts** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.22979)

49. **OptimAI: Optimization from Natural Language Using LLM-Powered AI Agents** Arxiv, 2025. [paper](https://arxiv.org/pdf/2504.16918)

50. **OptiHive: Ensemble Selection for LLM-Based Optimization via Statistical Modeling** Arxiv, 2025. [paper](https://arxiv.org/pdf/2508.02503)

51. **OPT-BENCH: Evaluating LLM Agent on Large-Scale Search Spaces Optimization Problems** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.10764), [code](https://github.com/OliverLeeXZ/OPT-BENCH)

52. **OpenEvolve: an open-source evolutionary coding agent** GitHub, 2025. [paper](https://huggingface.co/blog/codelion/openevolve), [code](https://github.com/algorithmicsuperintelligence/openevolve)

53. **Nested-Refinement Metamorphosis: Reflective Evolution for Efficient Optimization of Networking Problems** ACL, 2025. [paper](https://aclanthology.org/2025.findings-acl.895.pdf)

54. **MOTIF: Multi-strategy Optimization via Turn-based Interactive Framework** AAAI, 2025. [paper](https://arxiv.org/abs/2508.03929), [code](https://github.com/HaiAu2501/MOTIF)

55. **Monte Carlo Tree Search for Comprehensive Exploration in LLM-Based Automatic Heuristic Design** ICML, 2025. [paper](https://arxiv.org/pdf/2501.08603), [code](https://github.com/zz1358m/MCTS-AHD-master)

56. **MeLA: A Metacognitive LLM-Driven Architecture for Automatic Heuristic Design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2507.20541), [code](https://github.com/Qzs1335/MeLA)

57. **LLM4EO: Large Language Model for Evolutionary Optimization in Flexible Job Shop Scheduling** Arxiv, 2025. [paper](https://arxiv.org/pdf/2511.16485)

58. **LLM-QUBO: An End-to-End Framework for Automated QUBO Transformation from Natural Language Problem Descriptions** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.00099)

59. **LLM-Meta-SR: In-Context Learning for Evolving Selection Operators in Symbolic Regression** Arxiv, 2025. [paper](https://arxiv.org/abs/2505.18602)

60. **LLM-Driven Instance-Specific Heuristic Generation and Selection** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.00490)

61. **LLM-based Instance-driven Heuristic Bias in the Context of a Biased Random Key Genetic Algorithm** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.09707)

62. **Leveraging Large Language Models to Develop Heuristics for Emerging Optimization Problems** Arxiv, 2025. [paper](https://arxiv.org/pdf/2503.03350), [code](https://github.com/nico-koltermann/contextual-evolution-of-heuristics)

63. **Leveraging large language models for efficient scheduling in Human–Robot collaborative flexible manufacturing systems** npj Adv. Manuf., 2025. [paper](https://doi.org/10.1038/s44334-025-00061-w)

64. **Learn to Relax with Large Language Models: Solving Nonlinear Combinatorial Optimization Problems via Bidirectional Coevolution** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.12643)

65. **Large Language Models for Combinatorial Optimization: A Systematic Review** Arxiv, 2025. [paper](https://arxiv.org/pdf/2507.03637)

66. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://neurips.cc/virtual/2025/loc/san-diego/poster/115835), [code](https://github.com/Summer142857/LLMCoSolver)
    *Xia Jiang, Yaoxin Wu, Minshuo Li, Zhiguang Cao, Yingqian Zhang*

67. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://arxiv.org/pdf/2509.16865), [code](https://github.com/Summer142857/LLMCoSolver)

68. **Large Language Models and Operations Research: A Structured Survey** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.18180)

69. **LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.14138)

70. **Know the Ropes: A Heuristic Strategy for LLM-based Multi-Agent System Design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2505.16979)

71. **irace-evo: Automatic Algorithm Configuration Extended With LLM-Based Code Evolution** Arxiv, 2025. [paper](https://arxiv.org/pdf/2511.14794)

72. **Improving Existing Optimization Algorithms with LLMs** Arxiv, 2025. [paper](https://arxiv.org/pdf/2502.08298)

73. **HIFO-PROMPT: Prompting with Hindsight and Foresight For LLM-Based Automatic Heuristic Design** ICLR, 2025. [paper](https://arxiv.org/pdf/2508.13333)

74. **HeurAgenix: Leveraging LLMs for Solving Complex Combinatorial Optimization Challenges** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.15196), [code](https://github.com/microsoft/HeurAgenix)

75. **GraphThought: Graph Combinatorial Optimization with Thought Generation** Arxiv, 2025. [paper](https://arxiv.org/pdf/2502.11607)

76. **Glia: A Human-Inspired AI for Automated Systems Design and Optimization** Arxiv, 2025. [paper](https://arxiv.org/abs/2510.27176)

77. **Fitness Landscape of Large Language Model-Assisted Automated Algorithm Search** Arxiv, 2025. [paper](https://arxiv.org/pdf/2504.19636)

78. **Fine-tuning Large Language Model for Automated Algorithm Design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2507.10614)

79. **Experience-guided reflective co-evolution of prompts and heuristics for automatic algorithm design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.24509)

80. **EvoSpeak: Large Language Models for Interpretable Genetic Programming-Evolved Heuristics** Arxiv, 2025. [paper](https://arxiv.org/pdf/2510.02686)

81. **EvoCut: Strengthening Integer Programs via Evolution-Guided Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2508.11850), [code](https://github.com/milad1378yz/EvoCut)

82. **EquivaMap: Leveraging LLMs for Automatic Equivalence Checking of Optimization Formulations** Arxiv, 2025. [paper](https://arxiv.org/pdf/2502.14760), [code](https://github.com/HumainLab/EquivaMap)

83. **Efficient Heuristics Generation for Solving Combinatorial Optimization Problems Using Large Language Models** KDD, 2025. [paper](https://arxiv.org/pdf/2505.12627v1), [code](https://github.com/wuuu110/Hercules)

84. **EALG: Evolutionary Adversarial Generation of Language Model–Guided Generators for Combinatorial Optimization** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.02594)

85. **Discovering Heuristics with Large Language Models (LLMs) for Mixed-Integer Programs: Single-Machine Scheduling** Arxiv, 2025. [paper](https://arxiv.org/pdf/2510.24013)

86. **DHEvo: Data-Algorithm Based Heuristic Evolution for Generalizable MILP Solving** Arxiv, 2025. [paper](https://arxiv.org/pdf/2507.15615)

87. **DaSAThco: Data-Aware SAT Heuristics Combinations Optimization via Large Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.12602)

88. **CP-Bench: Evaluating Large Language Models for Constraint Modelling** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.06052)

89. **Combinatorial Optimization for All: Using LLMs to Aid Non-Experts in Improving Optimization Algorithms** Arxiv, 2025. [paper](https://arxiv.org/pdf/2503.10968), [code](https://github.com/camilochs/comb-opt-for-all)

90. **CogMCTS: A Novel Cognitive-Guided Monte Carlo Tree Search Framework for Iterative Heuristic Evolution with Large Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.08609)

91. **CodeEvolve: an open source evolutionary coding agent for algorithm discovery and optimization** Arxiv, 2025. [paper](https://arxiv.org/pdf/2510.14150), [code](https://github.com/inter-co/science-codeevolve)

92. **Code Evolution Graphs: Understanding Large Language Model Driven Design of Algorithms** GECCO, 2025. [paper](https://arxiv.org/pdf/2503.16668)

93. **CO-Bench: Benchmarking Language Model Agents in Algorithm Search for Combinatorial Optimization** AAAI, 2025. [paper](https://arxiv.org/pdf/2504.04310)

94. **Can Large Language Models Be Trusted as Black-Box Evolutionary Optimizers for Combinatorial Problems?** Arxiv, 2025. [paper](https://arxiv.org/pdf/2501.15081)

95. **CALM: Co-evolution of Algorithms and Language Model for Automatic Heuristic Design** ICLR, 2025. [paper](https://arxiv.org/pdf/2505.12285v1)

96. **Bridging Visualization and Optimization: Multimodal Large Language Models on Graph-Structured Combinatorial Optimization** Arxiv, 2025. [paper](https://arxiv.org/pdf/2501.11968)

97. **Behavior and Representation in Large Language Models for Combinatorial Optimization: From Feature Extraction to Algorithm Selection** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.13374)

98. **AutoPBO: LLM-powered Optimization for Local Search PBO Solvers** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.04007)

99. **Autonomous Code Evolution MeetsNP-Completeness** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.07367)

100. **Automatically discovering heuristics in a complex SAT solver with large language models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2507.22876)

101. **Automatic MILP Model Construction for Multi-Robot Task Allocation and Scheduling Based on Large Language Models** IROS, 2025. [paper](https://arxiv.org/pdf/2503.13813)

102. **AutoEP: LLMs-Driven Automation of Hyperparameter Evolution for Metaheuristic Algorithms** ICLR, 2025. [paper](https://arxiv.org/pdf/2509.23189)

103. **ARS: Automatic Routing Solver with Large Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2502.15359), [code](https://github.com/Ahalikai/ARS-Routbench)

104. **An Agentic Framework with LLMs for Solving Complex Vehicle Routing Problems** Arxiv, 2025. [paper](https://arxiv.org/pdf/2510.16701)

105. **AlphaEvolve: A coding agent for scientific and algorithmic discovery** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.13131), [code](https://colab.research.google.com/github/google-deepmind/alphaevolve_results/blob/master/mathematical_results.ipynb)

106. **Algorithm Discovery With LLMs: Evolutionary Search Meets Reinforcement Learning** COLM, 2025. [paper](https://arxiv.org/pdf/2504.05108)

107. **ALE-Bench: A Benchmark for Long-Horizon Objective-Driven Algorithm Engineering** NeurIPS 2025 Datasets and Benchmarks Track, 2025. [paper](https://arxiv.org/pdf/2506.09050), [code](https://github.com/SakanaAI/ALE-Bench)

108. **A Comprehensive Evaluation of Contemporary ML-Based Solvers for Combinatorial Optimization** ICML 2025 Workshop AI4Math, 2025. [paper](https://arxiv.org/pdf/2505.16952), [code](https://huggingface.co/datasets/CO-Bench/FrontierCO)

109. **Visual Reasoning and Multi-Agent Approach in Multimodal Large Language Models (MLLMs): Solving TSP and mTSP Combinatorial Challenges** Arxiv, 2024. [paper](https://arxiv.org/pdf/2407.00092), [code](https://github.com/ahmed-abdulhuy/Solving-TSP-and-mTSP-Combinatorial-Challenges-using-Visual-Reasoning-and-Multi-Agent-Approach-MLLMs-)

110. **UNCO: Towards Unifying Neural Combinatorial Optimization through Large Language Model** Arxiv, 2024. [paper](https://arxiv.org/pdf/2408.12214)

111. **Towards Foundation Models for Mixed Integer Linear Programming** ICLR, 2024. [paper](https://arxiv.org/pdf/2410.08288)

112. **Solving General Natural-Language-Description Optimization Problems with Large Language Models** NAACL, 2024. [paper](https://arxiv.org/pdf/2407.07924), [code](https://opt.alibabacloud.com/chat)

113. **Self-Guiding Exploration for Combinatorial Problems** NeurIPS, 2024. [paper](https://arxiv.org/pdf/2405.17950), [code](https://github.com/Zangir/LLM-for-CP)

114. **RouteExplainer: An Explanation Framework for Vehicle Routing Problem** PAKDD, 2024. [paper](https://arxiv.org/pdf/2403.03585.pdf), [code](https://github.com/ntt-dkiku/route-explainer)

115. **ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution** NeurIPS, 2024. [paper](https://arxiv.org/pdf/2402.01145), [code](https://github.com/ai4co/reevo)

116. **QUBE: Enhancing Automatic Heuristic Design via Quality-Uncertainty Balanced Evolution** Arxiv, 2024. [paper](https://arxiv.org/pdf/2412.20694), [code](https://github.com/zzjchen/QUBE_code)

117. **ORLM: Training Large Language Models for Optimization Modeling** Operations Research, 2024. [paper](https://arxiv.org/pdf/2405.17743), [code](https://github.com/Cardinal-Operations/ORLM)

118. **Multi-objective Evolution of Heuristic Using Large Language Model** AAAI, 2024. [paper](https://arxiv.org/pdf/2409.16867)

119. **LLMs can Schedule** Arxiv, 2024. [paper](https://arxiv.org/pdf/2408.06993), [code](https://github.com/starjob42/datasetjsp)

120. **LLMOPT: Learning to Define and Solve General Optimization Problems from Scratch** ICLR, 2024. [paper](https://arxiv.org/pdf/2410.13213)

121. **Large Language Models for Combinatorial Optimization of Design Structure Matrix** Arxiv, 2024. [paper](https://arxiv.org/pdf/2411.12571)

122. **HSEvo: Elevating Automatic Heuristic Design with Diversity-Driven Harmony Search and Genetic Algorithm Using LLMs** AAAI, 2024. [paper](https://arxiv.org/pdf/2412.14995), [code](https://github.com/datphamvn/HSEvo)

123. **How Multimodal Integration Boost the Performance of LLM for Optimization: Case Study on Capacitated Vehicle Routing Problems** Arxiv, 2024. [paper](https://arxiv.org/pdf/2403.01757)

124. **From Large Language Models and Optimization to Decision Optimization CoPilot: A Research Manifesto** Arxiv, 2024. [paper](https://arxiv.org/pdf/2402.16269)

125. **Eyeballing Combinatorial Problems: A Case Study of Using Multimodal Large Language Models to Solve Traveling Salesman Problems** ISBCom, 2024. [paper](https://arxiv.org/pdf/2406.06865)

126. **Evolution of Heuristics: Towards Efficient Automatic Algorithm Design Using Large Language Model** ICML, 2024. [paper](https://arxiv.org/pdf/2401.02051), [code](https://github.com/FeiLiu36/EoH)

127. **Evaluating LLM Reasoning in the Operations Research Domain with ORQA** AAAI, 2024. [paper](https://arxiv.org/pdf/2412.17874), [code](https://github.com/nl4opt/ORQA)

128. **Diagnosing Infeasible Optimization Problems Using Large Language Models** INFOR, 2024. [paper](https://arxiv.org/pdf/2308.12923)

129. **Can Large Language Models Solve Robot Routing?** Arxiv, 2024. [paper](https://arxiv.org/pdf/2403.10795), [code](https://github.com/Zhehui-Huang/LLM_Routing)

130. **AutoSAT: Automatically Optimize SAT Solvers via Large Language Models** Arxiv, 2024. [paper](https://arxiv.org/pdf/2402.10705)

131. **Automatic programming via large language models with population self-evolution for dynamic job shop scheduling problem** IEEE Trans. Fuzzy Syst., 2024. [paper](https://arxiv.org/pdf/2410.22657), [code](https://github.com/huangjin-collab/LHH_DFJSP_SeEvo)

132. **OptiMUS: Scalable Optimization Modeling with (MI)LP Solvers and Large Language Models** ICML, 2023. [paper](https://arxiv.org/pdf/2402.10172), [code](https://github.com/teshnizi/OptiMUS)

133. **NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes** ACL, 2023. [paper](https://arxiv.org/pdf/2312.14890), [code](https://github.com/casmlab/NPHardEval)

134. **Mathematical discoveries from program search with large language models** Nature, 2023. [paper](https://www.nature.com/articles/s41586-023-06924-6), [code](https://github.com/google-deepmind/funsearch)

135. **Large Language Models for Supply Chain Optimization** Arxiv, 2023. [paper](https://arxiv.org/pdf/2307.03875), [code](https://github.com/microsoft/OptiGuide)

136. **Large Language Models as Optimizers** ICLR, 2023. [paper](https://arxiv.org/pdf/2309.03409), [code](https://github.com/google-deepmind/opro)

137. **Large Language Models as Evolutionary Optimizers** CEC, 2023. [paper](https://arxiv.org/pdf/2310.19046), [code](https://github.com/cschen1205/LMEA)

138. **Chain-of-Experts: When LLMs Meet Complex Operations Research Problems** ICLR, 2023. [paper](https://openreview.net/pdf?id=HobyL1B9CZ), [code](https://github.com/xzymustbexzy/Chain-of-Experts)

139. **Can Language Models Solve Graph Problems in Natural Language?** NeurIPS, 2023. [paper](https://arxiv.org/pdf/2305.10037), [code](https://github.com/Arthur-Heng/NLGraph)

140. **Algorithm Evolution Using Large Language Model** Arxiv, 2023. [paper](https://arxiv.org/pdf/2311.15249)

141. **AI-Copilot for Business Optimisation: A Framework and A Case Study in Production Scheduling** Arxiv, 2023. [paper](https://arxiv.org/pdf/2309.13218), [code](https://github.com/pivithuruthejanamarasinghe/AI-Copilot-Data)

### [Survey Papers](#content) · *20 papers*

1. **Survey on Neural Routing Solvers** Arxiv, 2026. [paper](https://arxiv.org/abs/2602.21761)
    *Yunpeng Ba, Xi Lin, Changliang Zhou, Ruihao Zheng, Zhenkun Wang, Xinyan Liang, Zhichao Lu, Jianyong Sun, Yuhua Qian, Qingfu Zhang*

2. **Large Language Models for Combinatorial Optimization: A Systematic Review** Arxiv, 2025. [paper](https://arxiv.org/pdf/2507.03637)

3. **Applicability of Neural Combinatorial Optimization: A Critical View** TELO, 2024. [paper](https://dl.acm.org/doi/pdf/10.1145/3647644), [code](https://github.com/TheLeprechaun25/Applicability-NCO)
    *Andoni I. Garmendia, Josu Ceberio, Alexander Mendiburu*

4. **Combinatorial Optimization and Reasoning with Graph Neural Networks** JMLR, 2023. [paper](https://jmlr.org/papers/volume24/21-0449/21-0449.pdf)
    *Quentin Cappart, Didier Chetelat, Elias B. Khalil, Andrea Lodi, Christopher Morris, Petar Velickovic*

5. **A Survey for Solving Mixed Integer Programming via Machine Learning** Neurocomputing, 2022. [paper](https://www.sciencedirect.com/science/article/pii/S0925231222014035)
    *Jiayi Zhang, Chang Liu, Xijun Li, Hui-Ling Zhen, Mingxuan Yuan, Yawen Li, Junchi Yan*

6. **Machine Learning for Electronic Design Automation (EDA) : A Survey** TODAES, 2021. [paper](https://arxiv.org/abs/2102.03357)
    *Guyue Huang, Jingbo Hu, Yifan He, Jialong Liu, Mingyuan Ma, Zhaoyang Shen, Juejian Wu, Yuanfan Xu, Hengrui Zhang, Kai Zhong, others*

7. **Graph Learning for Combinatorial Optimization: A Survey of State-of-the-Art.** Data Science and Engineering, 2021. [paper](https://link.springer.com/article/10.1007/s41019-021-00155-3)
    *Yue Peng, Byron Choi, Jianliang Xu*

8. **Reinforcement Learning for Combinatorial Optimization: A Survey.** Arxiv, 2020. [paper](https://arxiv.org/abs/2003.03600)
    *Nina Mazyavkina, Sergey Sviridov, Sergei Ivanov, Evgeny Burnaev*

9. **Machine Learning for Combinatorial Optimization: a Methodological Tour d'horizon.** EJOR, 2020. [paper](https://arxiv.org/abs/1811.06128)
    *Yoshua Bengio, Andrea Lodi, Antoine Prouvost*

10. **Learning Graph Matching and Related Combinatorial Optimization Problems.** IJCAI, 2020. [paper](https://www.ijcai.org/proceedings/2020/0694.pdf)
    *Junchi Yan, Shuang Yang, Edwin R. Hancock*

11. **Learning Combinatorial Optimization on Graphs: A Survey with Applications to Networking.** IEEE ACCESS, 2020. [paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9125934)
    *Natalia Vesselinova, Rebecca Steinert, Daniel F. Perez-Ramirez, Magnus Boman*

12. **From Shallow to Deep Interactions Between Knowledge Representation, Reasoning and Machine Learning.** Arxiv, 2020. [paper](https://arxiv.org/abs/1912.06612)
    *Zied Bouraoui, Antoine Cornuéjols, Thierry Denœux, Sébastien Destercke, Didier Dubois, Romain Guillaume, João Marques-Silva, Jérôme Mengin, Henri Prade, Steven Schockaert, Mathieu Serrurier, Christel Vrain*

13. **A Survey on Reinforcement Learning for Combinatorial Optimization.** Arxiv, 2020. [paper](https://arxiv.org/abs/2008.12248v2)
    *Yunhao Yang, Andrew Whinston*

14. **A Review of combinatorial optimization with graph neural networks.** BigDIA, 2019. [paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8802843)
    *Tingfei Huang, Yang Ma, Yuzhen Zhou, Honglan Huang Huang, Dongmei Chen, Zidan Gong, Yao Liu*

15. **Machine Learning Approaches to Learning Heuristics for Combinatorial Optimization Problems.** Procedia Manufacturing, 2018. [paper](https://www.sciencedirect.com/science/article/pii/S2351978918311351)
    *Sadegh Mirshekarian, Dusan Sormaz*

16. **Deep Reinforcement Learning as a Job Shop Scheduling Solver: A Literature Review** Hybrid Intelligent Systems, 2018. [paper](http://link.springer.com/10.1007/978-3-030-14347-3_34)
    *Bruno Cunha, Ana M. Madureira, Benjamim Fonseca, Duarte Coelho*

17. **Boosting combinatorial problem modeling with machine learning.** IJCAI, 2018. [paper](https://www.ijcai.org/Proceedings/2018/0772.pdf)
    *Michele Lombardi, Michela Milano*

18. **A Survey of Reinforcement Learning and Agent-Based Approaches to Combinatorial Optimization.** Citeseer, 2012. [paper](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.468.5208&rep=rep1&type=pdf)
    *Victor Miagkikh*

19. **Model-Based Search for Combinatorial Optimization: A Critical Survey.** Annals of Operations Research, 2004. [paper](https://link.springer.com/article/10.1023/B:ANOR.0000039526.52305.af)
    *Mark Zlochin, Mauro Birattari, Nicolas Meuleau, Marco Dorigo*

20. **Neural Networks for Combinatorial Optimization: A Review of More Than a Decade of Research** INFORMS Journal on Computing, 1999. [paper](https://pubsonline.informs.org/doi/abs/10.1287/ijoc.11.1.15)
    *Kate A. Smith*

---

## [Problems](#content)

### [Job Shop Scheduling Problem](#content) · *42 papers*

1. **ReSched: Rethinking Flexible Job Shop Scheduling from a Transformer-based Architecture with Simplified States** ICLR, 2026. [paper](https://iclr.cc/virtual/2026/poster/10007089), [code](https://github.com/XiangjieXiao/ReSched)
    *Xiangjie Xiao, Zhiguang Cao, Cong Zhang, Wen Song*

2. **Multi-Action Self-Improvement for Neural Combinatorial Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2510.12273), [code](https://github.com/LTluttmann/macsim)
    *Laurin Luttmann, Lin Xie*

3. **LLM-Assisted Automatic Dispatching Rule Design for Dynamic Flexible Assembly Flow Shop Scheduling** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.15738)

4. **Heuristic Search as Language-Guided Program Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.16038)

5. **Hard Constraints Meet Soft Generation: Guaranteed Feasibility for LLM-based Combinatorial Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.01090)

6. **DyACE: Dynamic Algorithm Co-evolution for Online Automated Heuristic Design with Large Language Model** Arxiv, 2026. [paper](https://arxiv.org/pdf/2603.13344)

7. **DSevolve: Enabling Real-Time Adaptive Scheduling on Dynamic Shop Floor with LLM-Evolved Heuristic Portfolios** Arxiv, 2026. [paper](https://arxiv.org/pdf/2603.27628)

8. **TPD-AHD: Textual Preference Differentiation for LLM-Based Automatic Heuristic Design** Under Review, 2025. [paper](https://openreview.net/pdf?id=VEMknlIPtM)

9. **REMoH: A Reflective Evolution of Multi-objective Heuristics approach via Large Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.07759)

10. **ReflecSched: Solving Dynamic Flexible Job-Shop Scheduling via LLM-Powered Hierarchical Reflection** Arxiv, 2025. [paper](https://arxiv.org/pdf/2508.01724)

11. **LLM4EO: Large Language Model for Evolutionary Optimization in Flexible Job Shop Scheduling** Arxiv, 2025. [paper](https://arxiv.org/pdf/2511.16485)

12. **Leveraging large language models for efficient scheduling in Human–Robot collaborative flexible manufacturing systems** npj Adv. Manuf., 2025. [paper](https://doi.org/10.1038/s44334-025-00061-w)

13. **Learn to Relax with Large Language Models: Solving Nonlinear Combinatorial Optimization Problems via Bidirectional Coevolution** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.12643)

14. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://neurips.cc/virtual/2025/loc/san-diego/poster/115835), [code](https://github.com/Summer142857/LLMCoSolver)
    *Xia Jiang, Yaoxin Wu, Minshuo Li, Zhiguang Cao, Yingqian Zhang*

15. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://arxiv.org/pdf/2509.16865), [code](https://github.com/Summer142857/LLMCoSolver)

16. **HeurAgenix: Leveraging LLMs for Solving Complex Combinatorial Optimization Challenges** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.15196), [code](https://github.com/microsoft/HeurAgenix)

17. **Glia: A Human-Inspired AI for Automated Systems Design and Optimization** Arxiv, 2025. [paper](https://arxiv.org/abs/2510.27176)

18. **Foundation Models for Industrial Scheduling Leveraging the Techniques from LLMs** Under Review, 2025. [paper](https://openreview.net/pdf?id=qRjLjYrvMi)

19. **EvoSpeak: Large Language Models for Interpretable Genetic Programming-Evolved Heuristics** Arxiv, 2025. [paper](https://arxiv.org/pdf/2510.02686)

20. **Discovering Heuristics with Large Language Models (LLMs) for Mixed-Integer Programs: Single-Machine Scheduling** Arxiv, 2025. [paper](https://arxiv.org/pdf/2510.24013)

21. **ACCORD: Autoregressive Constraint-satisfying Generation for COmbinatorial Optimization with Routing and Dynamic attention** Under Review, 2025. [paper](https://openreview.net/pdf?id=f0TBAdcJ8m)

22. **A Comprehensive Evaluation of Contemporary ML-Based Solvers for Combinatorial Optimization** ICML 2025 Workshop AI4Math, 2025. [paper](https://arxiv.org/pdf/2505.16952), [code](https://huggingface.co/datasets/CO-Bench/FrontierCO)

23. **STARJOB: Dataset for LLM-Driven Job Shop Scheduling** Under Review, 2024. [paper](https://openreview.net/forum?id=t0fU6t3Skw)

24. **Self-Guiding Exploration for Combinatorial Problems** NeurIPS, 2024. [paper](https://arxiv.org/pdf/2405.17950), [code](https://github.com/Zangir/LLM-for-CP)

25. **LLMs can Schedule** Arxiv, 2024. [paper](https://arxiv.org/pdf/2408.06993), [code](https://github.com/starjob42/datasetjsp)

26. **GOAL: A Generalist Combinatorial Optimization Agent Learner** ICLR, 2024. [paper](https://arxiv.org/pdf/2406.15079), [code](https://github.com/naver/goal-co)

27. **Automatic programming via large language models with population self-evolution for dynamic job shop scheduling problem** IEEE Trans. Fuzzy Syst., 2024. [paper](https://arxiv.org/pdf/2410.22657), [code](https://github.com/huangjin-collab/LHH_DFJSP_SeEvo)

28. **Applicability of Neural Combinatorial Optimization: A Critical View** TELO, 2024. [paper](https://dl.acm.org/doi/pdf/10.1145/3647644), [code](https://github.com/TheLeprechaun25/Applicability-NCO)
    *Andoni I. Garmendia, Josu Ceberio, Alexander Mendiburu*

29. **Winner Takes It All: Training Performant RL Populations for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=v6VpqGcGAR)
    *Nathan Grinsztajn, Daniel Furelos-Blanco, Shikha Surana, Cl{\'e}ment Bonnet, Thomas D Barrett*

30. **Robust Scheduling with GFlowNets** ICLR, 2023. [paper](https://openreview.net/forum?id=ZBUthI6wK9h)
    *David W Zhang, Corrado Rainone, Markus Peschl, Roberto Bondesan*

31. **Neural DAG Scheduling via One-Shot Priority Sampling** ICLR, 2023. [paper](https://openreview.net/forum?id=WL8FlAugqQ)
    *Wonseok Jeon, Mukul Gagrani, Burak Bartan, Weiliang Will Zeng, Harris Teague, Piero Zappi, Christopher Lott*

32. **DeepACO: Neural-enhanced Ant Systems for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=cd5D1DD923), [code](https://github.com/henry-yeh/DeepACO)
    *Haoran Ye, Jiarui Wang, Zhiguang Cao, Helan Liang, Yong Li*

33. **Continual Task Allocation in Meta-Policy Network via Sparse Prompting** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/24080)
    *Yijun, Tianyi Zhou, Jing Jiang, Guodong Long Yang, Yuhui Shi.*

34. **Combinatorial Optimization with Policy Adaptation using Latent Space Search** NeurIPS, 2023. [paper](https://openreview.net/forum?id=vpMBqdt9Hl)
    *Felix Chalumeau, Shikha Surana, Cl{\'e}ment Bonnet, Nathan Grinsztajn, Arnu Pretorius, Alexandre Laterre, Thomas D Barrett*

35. **AI-Copilot for Business Optimisation: A Framework and A Case Study in Production Scheduling** Arxiv, 2023. [paper](https://arxiv.org/pdf/2309.13218), [code](https://github.com/pivithuruthejanamarasinghe/AI-Copilot-Data)

36. **ScheduleNet: Learn to Solve Multi-agent Scheduling Problems with Reinforcement Learning** Arxiv, 2021. [paper](https://arxiv.org/abs/2106.03051)
    *Junyoung Park, Sanjar Bakhtiyar, Jinkyoo Park*

37. **Learning to schedule job-shop problems: Representation and policy learning using graph neural network and reinforcement learning.** International Journal of Production Research, 2021. [paper](https://arxiv.org/abs/2106.01086)
    *Junyoung Park, Jaehyeong Chun, Sang Hun Kim, Youngkook Kim, Jinkyoo Park*

38. **Explainable reinforcement learning in production control of job shop manufacturing system.** International Journal of Production Research, 2021. [paper](https://www.tandfonline.com/doi/abs/10.1080/00207543.2021.1972179?journalCode=tprs20)
    *Andreas Kuhnle, Marvin Carl May, Louis Sch?fer, Gisela Lanza*

39. **Dynamic job-shop scheduling in smart manufacturing using deep reinforcement learning** Computer Networks, 2021. [paper](https://www.sciencedirect.com/science/article/pii/S1389128621001031)
    *Libing Wang, Xin Hu, Yin Wang, Sujie Xu, Shijun Ma, Kexin Yang, Zhijun Liu, Weidong Wang*

40. **Learning to Dispatch for Job Shop Scheduling via Deep Reinforcement Learning.** NeurIPS, 2020. [paper](https://arxiv.org/abs/2010.12367), [code](https://github.com/zcajiayin/L2D)
    *Cong Zhang, Wen Song, Zhiguang Cao, Jie Zhang, Puay Siew Tan, Chi Xu*

41. **Smart Manufacturing Scheduling With Edge Computing Using Multiclass Deep Q Network** Transactions on Industrial Informatics, 2019. [paper](https://ieeexplore.ieee.org/document/8676376)
    *Chun-Cheng Lin, Der-Jiunn Deng, Yen-Ling Chih, Hsin-Ting Chiu*

42. **Multi-Agent Reinforcement Learning for Job Shop Scheduling in Flexible Manufacturing Systems** International Conference on Artificial Intelligence for Industries (AI4I), 2019. [paper](https://ieeexplore.ieee.org/document/9027776)
    *Schirin Baer, Jupiter Bakakeu, Richard Meyes, Tobias Meisen*

### [Flow Shop Problem](#content) · *12 papers*

1. **Multi-Action Self-Improvement for Neural Combinatorial Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2510.12273), [code](https://github.com/LTluttmann/macsim)
    *Laurin Luttmann, Lin Xie*

2. **LLM-Assisted Automatic Dispatching Rule Design for Dynamic Flexible Assembly Flow Shop Scheduling** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.15738)

3. **Hard Constraints Meet Soft Generation: Guaranteed Feasibility for LLM-based Combinatorial Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.01090)

4. **Planning of Heuristics: Strategic Planning on Large Language Models with Monte Carlo Tree Search for Automating Heuristic Optimization** Arxiv, 2025. [paper](https://arxiv.org/pdf/2502.11422)

5. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://arxiv.org/pdf/2509.16865), [code](https://github.com/Summer142857/LLMCoSolver)

6. **HIFO-PROMPT: Prompting with Hindsight and Foresight For LLM-Based Automatic Heuristic Design** ICLR, 2025. [paper](https://arxiv.org/pdf/2508.13333)

7. **Hierarchical Representations for Cross-task Automated Heuristic Design using LLMs** Under Review, 2025. [paper](https://openreview.net/pdf?id=dgvx86qybJ)

8. **AutoEP: LLMs-Driven Automation of Hyperparameter Evolution for Metaheuristic Algorithms** ICLR, 2025. [paper](https://arxiv.org/pdf/2509.23189)

9. **Algorithm Discovery With LLMs: Evolutionary Search Meets Reinforcement Learning** COLM, 2025. [paper](https://arxiv.org/pdf/2504.05108)

10. **ACCORD: Autoregressive Constraint-satisfying Generation for COmbinatorial Optimization with Routing and Dynamic attention** Under Review, 2025. [paper](https://openreview.net/pdf?id=f0TBAdcJ8m)

11. **Solving Diverse Combinatorial Optimization Problems with a Unified Model** Under Review, 2024. [paper](https://openreview.net/forum?id=Kc3yoIL5oR)

12. **Evolution of Heuristics: Towards Efficient Automatic Algorithm Design Using Large Language Model** ICML, 2024. [paper](https://arxiv.org/pdf/2401.02051), [code](https://github.com/FeiLiu36/EoH)

### [Sorting & Ranking](#content) · *15 papers*

1. **LLM-Meta-SR: In-Context Learning for Evolving Selection Operators in Symbolic Regression** Arxiv, 2025. [paper](https://arxiv.org/abs/2505.18602)

2. **GOAL: A Generalist Combinatorial Optimization Agent Learner** ICLR, 2024. [paper](https://arxiv.org/pdf/2406.15079), [code](https://github.com/naver/goal-co)

3. **Applicability of Neural Combinatorial Optimization: A Critical View** TELO, 2024. [paper](https://dl.acm.org/doi/pdf/10.1145/3647644), [code](https://github.com/TheLeprechaun25/Applicability-NCO)
    *Andoni I. Garmendia, Josu Ceberio, Alexander Mendiburu*

4. **Neural Improvement Heuristics for Graph Combinatorial Optimization Problems** TNNLS, 2023. [paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10271315&casa_token=Hqn_wH2HAjEAAAAA:rTd6KVaoKVjrFWASa-Ma0vC6CBvsmMUHnoWik2DyD56NbnfNOqBG5qZTBLR5hqf9vpCotivB_BU&tag=1), [code](https://github.com/TheLeprechaun25/neural-improvement-heuristics)
    *Andoni I. Garmendia, Josu Ceberio, Alexander Mendiburu*

5. **PiRank-Scalable Learning To Rank via Differentiable Sorting** NeurIPS, 2022. [paper](https://openreview.net/forum?id=dL8p6rLFTS3), [code](https://github.com/ermongroup/pirank)
    *Robin Marcel Edwin Swezey, Aditya Grover, Bruno Charron, Stefano Ermon*

6. **Decision-Focused Learning: Through the Lens of Learning to Rank** ICML, 2022. [paper](https://proceedings.mlr.press/v162/mandi22a.html), [code](https://github.com/jayman91/ltr-predopt)
    *Jayanta Mandi, Vı́ctor Bucarey, Maxime Mulamba Ke Tchomba, Tias Guns*

7. **Automatic Loss Function Search for Predict-Then-Optimize Problems with Strong Ranking Property** ICLR, 2022. [paper](https://openreview.net/forum?id=hSktDu-h94), [code](https://github.com/Microsoft/AutoPredOptConnector)
    *Boshi Wang, Jialin Yi, Hang Dong, Bo Qiao, Chuan Luo, Qingwei Lin*

8. **SoftSort: A Continuous Relaxation for the argsort Operator** ICML, 2020. [paper](http://proceedings.mlr.press/v119/prillo20a/prillo20a.pdf), [code](https://github.com/sprillo/softsort)
    *Sebastian Prillo, Julian Martin Eisenschlos*

9. **Optimizing Rank-Based Metrics With Blackbox Differentiation** CVPR, 2020. [paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Rolinek_Optimizing_Rank-Based_Metrics_With_Blackbox_Differentiation_CVPR_2020_paper.pdf), [code](https://github.com/martius-lab/blackbox-backprop)
    *Marin Vlastelica, Anselm Paulus, Vít Musil, Georg Martius, Michal Rolínek*

10. **Fast Differentiable Sorting and Ranking** ICML, 2020. [paper](http://proceedings.mlr.press/v119/blondel20a/blondel20a.pdf), [code](https://github.com/google-research/fast-soft-sort/)
    *Mathieu Blondel Olivier Teboul Quentin Berthet Josip Djolonga*

11. **differentiable top k with optimal transport** NeurIPS, 2020. [paper](https://proceedings.neurips.cc/paper/2020/hash/ec24a54d62ce57ba93a531b460fa8d18-Abstract.html)
    *Yujia Xie, Hanjun Dai, Minshuo Chen, Bo Dai, Tuo Zhao, Hongyuan Zha, Wei Wei, Tomas Pfister*

12. **Stochastic Optimization of Sorting Networks via Continuous Relaxations** ICLR, 2019. [paper](https://openreview.net/forum?id=H1eSS3CcKX), [code](https://github.com/ermongroup/neuralsort)
    *Aditya Grover, Eric Wang, Aaron Zweig, Stefano Ermon*

13. **Predict+optimise with ranking objectives: exhaustively learning linear functions** IJCAI, 2019. [paper](https://dl.acm.org/doi/abs/10.5555/3367032.3367186)
    *Emir Demirovic, Peter J. Stuckey, James Bailey, Jeffrey Chan, Christopher Leckie, Kotagiri Ramamohanarao, Tias Guns*

14. **Differentiable Ranking and Sorting using Optimal Transport** NeurIPS, 2019. [paper](https://papers.nips.cc/paper/2019/hash/d8c24ca8f23c562a5600876ca2a550ce-Abstract.html)
    *Marco Cuturi, Olivier Teboul, Jean-Philippe Vert*

15. **Ranking via sinkhorn propagation** Arxiv, 2011. [paper](https://arxiv.org/abs/1106.1925#)
    *Ryan Prescott Adams, Richard S. Zemel*

### [Graph Matching](#content) · *28 papers*

1. **Learning to Prune Instances of Steiner Tree Problem in Grap** INOC, 2024. [paper](https://openproceedings.org/2024/conf/inoc/INOC_31.pdf), [code](https://github.com/dajwani/alenex22)
    *Jiwei Zhang, Dena Tayebi, Saurabh Ray, Deepak Ajwani*

2. **Learning General Representations Across Graph Combinatorial Optimization Problems** Under Review, 2024. [paper](https://openreview.net/forum?id=elmTU101oS)

3. **SeedGNN: Graph Neural Network for Supervised Seeded Graph Matching** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/24282)
    *Liren Yu, Jiaming Xu, Xiaojun Lin*

4. **Revocable Deep Reinforcement Learning with Affinity Regularization for Outlier-Robust Graph Matching.** ICLR, 2023. [paper](https://openreview.net/forum?id=QjQibO3scV_), [code](https://github.com/Thinklab-SJTU/RGM)
    *Chang Liu, Zetian Jiang, Runzhong Wang, Junchi Yan, Lingxiao Huang, Pinyan Lu*

5. **LVM-Med: Learning Large-Scale Self-Supervised Vision Models for Medical Imaging via Second-order Graph Matching** NeurIPS, 2023. [paper](https://openreview.net/forum?id=xE7oH5iVGK), [code](https://github.com/duyhominhnguyen/LVM-Med)
    *Duy MH Nguyen, Hoang Nguyen, Nghiem T Diep, Tan N Pham, Tri Cao, Binh T Nguyen, Paul Swoboda, Nhat Ho, Shadi Albarqouni, Pengtao Xie, others*

6. **LinSATNet: The Positive Linear Satisfiability Neural Networks** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25110), [code](https://github.com/Thinklab-SJTU/LinSATNet)
    *Runzhong Wang, Yunhao Zhang, Ziao Guo, Tianyi Chen, Xiaokang Yang, Junchi Yan*

7. **Improving Graph Matching with Positional Reconstruction Encoder-Decoder Network** NeurIPS, 2023. [paper](https://openreview.net/forum?id=28RTu9MOT6)
    *Yixiao Zhou, Ruiqi Jia, Hongxiang Lin, Hefeng Quan, Yumeng Zhao, Xiaoqing Lyu*

8. **D2Match: Leveraging Deep Learning and Degeneracy for Subgraph Matching** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/24358)
    *Xuan Liu, Lin Zhang, Jiaqi Sun, Yujiu Yang, Haiqing Yang*

9. **Can Language Models Solve Graph Problems in Natural Language?** NeurIPS, 2023. [paper](https://arxiv.org/pdf/2305.10037), [code](https://github.com/Arthur-Heng/NLGraph)

10. **Self-supervised Learning of Visual Graph Matching** ECCV, 2022. [paper](https://link.springer.com/chapter/10.1007/978-3-031-20050-2_22), [code](https://github.com/Thinklab-SJTU/ThinkMatch-SCGM)
    *Chang Liu, Shaofeng Zhang, Xiaokang Yang, Junchi Yan*

11. **Appearance and Structure Aware Robust Deep Visual Graph Matching: Attack, Defense and Beyond** CVPR, 2022. [paper](https://openaccess.thecvf.com/content/CVPR2022/papers/Ren_Appearance_and_Structure_Aware_Robust_Deep_Visual_Graph_Matching_Attack_CVPR_2022_paper.pdf), [code](https://github.com/Thinklab-SJTU/RobustMatch)
    *Qibing Ren, Qingquan Bao, Runzhong Wang, Junchi Yan*

12. **Neural Graph Matching Network: Learning Lawler's Quadratic Assignment Problem with Extension to Hypergraph and Multiple-graph Matching.** TPAMI, 2021. [paper](https://arxiv.org/abs/1911.11308), [code](https://github.com/Thinklab-SJTU/ThinkMatch)
    *Runzhong Wang, Junchi Yan, Xiaokang Yang*

13. **Learning to Match Features with Seeded Graph Matching Network** ICCV, 2021. [paper](https://openaccess.thecvf.com/content/ICCV2021/html/Chen_Learning_To_Match_Features_With_Seeded_Graph_Matching_Network_ICCV_2021_paper.html)
    *Hongkai Chen, Zixin Luo, Jiahui Zhang, Lei Zhou, Xuyang Bai, Zeyu Hu, Chiew-Lan Tai, Long Quan*

14. **IA-GM: A Deep Bidirectional Learning Method for Graph Matching** AAAI, 2021. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/16461/16268)
    *Kaixuan Zhao, Shikui Tu, Lei Xu*

15. **Hypergraph Neural Networks for Hypergraph Matching** ICCV, 2021. [paper](https://openaccess.thecvf.com/content/ICCV2021/papers/Liao_Hypergraph_Neural_Networks_for_Hypergraph_Matching_ICCV_2021_paper.pdf)
    *Xiaowei Liao, Yong Xu, Haibin Ling*

16. **GAMnet: Robust Feature Matching via Graph Adversarial-Matching Network** MM, 2021. [paper](https://dl.acm.org/doi/pdf/10.1145/3474085.3475669)
    *Bo Jiang, Pengfei Sun, Ziyan Zhang, Jin Tang, Bin Luo*

17. **Deep Latent Graph Matching** ICML, 2021. [paper](http://proceedings.mlr.press/v139/yu21d/yu21d.pdf)
    *Tianshu Yu, Runzhong Wang, Junchi Yan, Baoxin Li*

18. **Deep Graph Matching under Quadratic Constraint** CVPR, 2021. [paper](https://openaccess.thecvf.com/content/CVPR2021/papers/Gao_Deep_Graph_Matching_Under_Quadratic_Constraint_CVPR_2021_paper.pdf)
    *Quankai Gao, Fudong Wang, Nan Xue, Jin-Gang Yu, Gui-Song Xia*

19. **Learning deep graph matching with channel-independent embedding and Hungarian attention.** ICLR, 2020. [paper](https://openreview.net/forum?id=rJgBd2NYPH), [code](https://github.com/Thinklab-SJTU/ThinkMatch)
    *Tianshu Yu, Runzhong Wang, Junchi Yan, Baoxin Li*

20. **Graduated Assignment for Joint Multi-Graph Matching and Clustering with Application to Unsupervised Graph Matching Network Learning.** NeurIPS, 2020. [paper](https://papers.NeurIPS.cc/paper/2020/file/e6384711491713d29bc63fc5eeb5ba4f-Paper.pdf), [code](https://github.com/Thinklab-SJTU/ThinkMatch)
    *Runzhong Wang, Junchi Yan, Xiaokang Yang*

21. **Deep Graph Matching via Blackbox Differentiation of Combinatorial Solvers.** ECCV, 2020. [paper](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123730409.pdf), [code](https://github.com/martius-lab/blackbox-deep-graph-matching)
    *Michal Rolinek, Paul Swoboda, Dominik Zietlow, Anselm Paulus, Vit Musil, Georg Martius*

22. **Deep Graph Matching Consensus.** ICLR, 2020. [paper](http://arxiv.org/abs/2001.09621)
    *Matthias Fey, Jan E. Lenssen, Christopher Morris, Jonathan Masci, Nils M. Kriege*

23. **Combinatorial Learning of Robust Deep Graph Matching: An Embedding Based Approach.** TPAMI, 2020. [paper](https://doi.org/10.1109/TPAMI.2020.3005590), [code](https://github.com/Thinklab-SJTU/ThinkMatch)
    *Runzhong Wang, Junchi Yan, Xiaokang Yang*

24. **Learning Combinatorial Embedding Networks for Deep Graph Matching.** ICCV, 2019. [paper](http://openaccess.thecvf.com/content_ICCV_2019/papers/Wang_Learning_Combinatorial_Embedding_Networks_for_Deep_Graph_Matching_ICCV_2019_paper.pdf), [code](https://github.com/Thinklab-SJTU/ThinkMatch)
    *Runzhong Wang, Junchi Yan, Xiaokang Yang*

25. **GLMNet: Graph Learning-Matching Networks for Feature Matching.** Arxiv, 2019. [paper](https://arxiv.org/abs/1911.07681)
    *Bo Jiang, Pengfei Sun, Jin Tang, Bin Luo*

26. **Deep Graphical Feature Learning for the Feature Matching Problem.** ICCV, 2019. [paper](https://openaccess.thecvf.com/content_ICCV_2019/papers/Zhang_Deep_Graphical_Feature_Learning_for_the_Feature_Matching_Problem_ICCV_2019_paper.pdf)
    *Zhen Zhang, Wee Sun Lee*

27. **Deep Learning of Graph Matching.** CVPR, 2018. [paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Zanfir_Deep_Learning_of_CVPR_2018_paper.html)
    *Andrei Zanfir, Cristian Sminchisescu*

28. **Revised Note on Learning Algorithms for Quadratic Assignment with Graph Neural Networks** Arxiv, 2017. [paper](https://arxiv.org/pdf/1706.07450.pdf), [code](https://github.com/alexnowakvila/QAP_pt)
    *Alex Nowak, Soledad Villar, S. Afonso Bandeira, Joan Bruna*

### [Quadratic Assignment Problem](#content) · *4 papers*

1. **Towards Quantum Machine Learning for Constrained Combinatorial Optimization: a Quantum QAP Solver** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/24148)
    *Xinyu Ye, Ge Yan, Junchi Yan*

2. **Revocable Deep Reinforcement Learning with Affinity Regularization for Outlier-Robust Graph Matching.** ICLR, 2023. [paper](https://openreview.net/forum?id=QjQibO3scV_), [code](https://github.com/Thinklab-SJTU/RGM)
    *Chang Liu, Zetian Jiang, Runzhong Wang, Junchi Yan, Lingxiao Huang, Pinyan Lu*

3. **Neural Graph Matching Network: Learning Lawler's Quadratic Assignment Problem with Extension to Hypergraph and Multiple-graph Matching.** TPAMI, 2021. [paper](https://arxiv.org/abs/1911.11308), [code](https://github.com/Thinklab-SJTU/ThinkMatch)
    *Runzhong Wang, Junchi Yan, Xiaokang Yang*

4. **Revised Note on Learning Algorithms for Quadratic Assignment with Graph Neural Networks** Arxiv, 2017. [paper](https://arxiv.org/pdf/1706.07450.pdf), [code](https://github.com/alexnowakvila/QAP_pt)
    *Alex Nowak, Soledad Villar, S. Afonso Bandeira, Joan Bruna*

### [Travelling Salesman Problem](#content) · *149 papers*

1. **ViTSP: A Vision Language Models Guided Framework for Solving Large-Scale Traveling Salesman Problems** ICLR, 2026. [paper](https://arxiv.org/abs/2509.23465), [code](https://github.itap.purdue.edu/uSMART/ViTSP_ICLR2026)
    *Zhuoli Yin, Yi Ding, Reem Khir, Hua Cai*

2. **Towards Efficient Constraint Handling in Neural Solvers for Routing Problems** ICLR, 2026. [paper](https://openreview.net/forum?id=raDFGuQxvD), [code](https://github.com/jieyibi/CaR-constraint)
    *Jieyi Bi, Zhiguang Cao, Jianan Zhou, Wen Song, Yaoxin Wu, Jie Zhang, Yining Ma, Cathy Wu*

3. **Rethinking LLM-Driven Heuristic Design: Generating Efficient and Specialized Solvers via Dynamics-Aware Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.20868)

4. **PathWise: Planning through World Model for Automated Heuristic Design via Self-Evolving LLMs** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.20539)

5. **Native Adaptive Solution Expansion for Diffusion-based Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=084SvT55yk)
    *Yu Wang, Yang Li, Jiale Ma, Junchi Yan, Yi Chang*

6. **MaskCO: Masked Generation Drives Effective Representation Learning and Exploiting for Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=psUjNnLhl9), [code](https://github.com/Thinklab-SJTU/MaskCO)
    *Lvda Chen, Yang Li, Junchi Yan*

7. **HeuriGym: An Agentic Benchmark for LLM-Crafted Heuristics in Combinatorial Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2506.07972), [code](https://github.com/cornell-zhang/heurigym)
    *Hongzheng Chen, Yingheng Wang, Yaohui Cai, Hins Hu, Jiajie Li, Shirley Huang, Chenhui Deng, Rongjian Liang, Shufeng Kong, Haoxing Ren, Samitha Samaranayake, Carla P. Gomes, Zhiru Zhang*

8. **Hard Constraints Meet Soft Generation: Guaranteed Feasibility for LLM-based Combinatorial Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.01090)

9. **Generalizable Heuristic Generation Through LLMs with Meta-Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2505.20881), [code](https://github.com/yiding-s/MoH)
    *Yiding Shi, Jianan Zhou, Wen Song, Jieyi Bi, Yaoxin Wu, Zhiguang Cao, Jie Zhang*

10. **Game-Theoretic Co-Evolution for LLM-Based Heuristic Discovery** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.22896)

11. **G-LNS: Generative Large Neighborhood Search for LLM-Based Automatic Heuristic Design** Arxiv, 2026. [paper](https://arxiv.org/abs/2602.08253), [code](https://github.com/ZBoyn/G-LNS)
    *Baoyun Zhao, He Wang, Liang Zeng*

12. **FrontierCO: Real-World and Large-Scale Evaluation of Machine Learning Solvers for Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=BVprkacwFY), [code](https://github.com/sunnweiwei/FrontierCO)
    *Shengyu Feng, Weiwei Sun, Shanda Li, Ameet Talwalkar, Yiming Yang*

13. **EoH-S: Evolution of Heuristic Set using LLMs for Automated Heuristic Design** AAAI, 2026. [paper](https://arxiv.org/abs/2508.03082), [code](https://github.com/FeiLiu36/EoH-S)
    *Fei Liu, Yilu Liu, Qingfu Zhang, Xialiang Tong, Mingxuan Yuan*

14. **DyACE: Dynamic Algorithm Co-evolution for Online Automated Heuristic Design with Large Language Model** Arxiv, 2026. [paper](https://arxiv.org/pdf/2603.13344)

15. **DRAGON: LLM-Driven Decomposition and Reconstruction Agents for Large-Scale Combinatorial Optimization** AAMAS, 2026. [paper](https://arxiv.org/abs/2601.06502)
    *Shengkai Chen, Zhiguang Cao, Jianan Zhou, Yaoxin Wu, Senthilnath Jayavelu, Zhuoyi Lin, Xiaoli Li, Shili Xiang*

16. **CDEoH: Category-Driven Automatic Algorithm Design With Large Language Models** Arxiv, 2026. [paper](https://arxiv.org/pdf/2603.19284)

17. **Bridging Synthetic and Real Routing Problems via LLM-Guided Instance Generation and Progressive Adaptation** AAAI, 2026. [paper](https://arxiv.org/abs/2511.10233), [code](https://github.com/HenryZhu1029/EvoReal)
    *Jianghan Zhu, Yaoxin Wu, Zhuoyi Lin, Zhengyuan Zhang, Haiyan Yin, Zhiguang Cao, Senthilnath Jayavelu, Xiaoli Li*

18. **Beyond the Node: Clade-level Selection for Efficient MCTS in Automatic Heuristic Design** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.00549)

19. **Beyond Simple Graphs: Neural Multi-Objective Routing on Multigraphs** ICLR, 2026. [paper](https://arxiv.org/abs/2506.22095), [code](https://github.com/filiprydin/GMS)
    *Filip Rydin, Attila Lischka, Jiaming Wu, Morteza Haghir Chehreghani, Balazs Kulcsar*

20. **Unify ML4TSP: Drawing Methodological Principles for TSP and Beyond from Streamlined Design Space of Learning and Search** ICLR, 2025. [paper](https://openreview.net/pdf?id=grU1VKEOLi), [code](https://github.com/Thinklab-SJTU/ML4TSPBench)
    *Yang Li, Jiale Ma, Wenzheng Pan, Runzhong Wang, Haoyu Geng, Nianzu Yang, Junchi Yan*

21. **UniCO: On Unified Combinatorial Optimization via Problem Reduction to Matrix-Encoded General TSP** ICLR, 2025. [paper](https://openreview.net/forum?id=yEwakMNIex), [code](https://github.com/Thinklab-SJTU/UniCO)
    *Wenzheng Pan, Hao Xiong, Jiale Ma, Wentao Zhao, Yang Li, Junchi Yan*

22. **TPD-AHD: Textual Preference Differentiation for LLM-Based Automatic Heuristic Design** Under Review, 2025. [paper](https://openreview.net/pdf?id=VEMknlIPtM)

23. **RoCo: Role-Based LLMs Collaboration for Automatic Heuristic Design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.03762)

24. **Rethinking Neural Multi-Objective Combinatorial Optimization via Neat Weight Embedding** ICLR, 2025. [paper](https://openreview.net/forum?id=GM7cmQfk2F)
    *Jinbiao Chen, Zhiguang Cao, Jiahai Wang, Yaoxin Wu, Hanzhang Qin, Zizhen Zhang, Yue-Jiao Gong*

25. **Rethinking Code Similarity for Automated Algorithm Design with LLMs** ICLR, 2025. [paper](https://openreview.net/pdf?id=HIUqeO9OOr)

26. **RedAHD: Reduction-Based End-to-End Automatic Heuristic Design with Large Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2505.20242)

27. **Planning of Heuristics: Strategic Planning on Large Language Models with Monte Carlo Tree Search for Automating Heuristic Optimization** Arxiv, 2025. [paper](https://arxiv.org/pdf/2502.11422)

28. **Pareto-Grid-Guided Large Language Models for Fast and High-Quality Heuristics Design in Multi-Objective Combinatorial Optimization** AAAI, 2025. [paper](https://arxiv.org/pdf/2507.20923), [code](https://github.com/langkhachhoha/MPaGE)

29. **OPT-BENCH: Evaluating LLM Agent on Large-Scale Search Spaces Optimization Problems** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.10764), [code](https://github.com/OliverLeeXZ/OPT-BENCH)

30. **Neural Multi-Objective Combinatorial Optimization via Graph-Image Multimodal Fusion** ICLR, 2025. [paper](https://openreview.net/forum?id=4sJ2FYE65U)
    *Jinbiao Chen, Jiahai Wang, Zhiguang Cao, Yaoxin Wu*

31. **Nested-Refinement Metamorphosis: Reflective Evolution for Efficient Optimization of Networking Problems** ACL, 2025. [paper](https://aclanthology.org/2025.findings-acl.895.pdf)

32. **MOTIF: Multi-strategy Optimization via Turn-based Interactive Framework** AAAI, 2025. [paper](https://arxiv.org/abs/2508.03929), [code](https://github.com/HaiAu2501/MOTIF)

33. **Monte Carlo Tree Search for Comprehensive Exploration in LLM-Based Automatic Heuristic Design** ICML, 2025. [paper](https://arxiv.org/pdf/2501.08603), [code](https://github.com/zz1358m/MCTS-AHD-master)

34. **ML4CO-Bench-101: Benchmark Machine Learning for Classic Combinatorial Problems on Graphs** NeurIPS, 2025. [paper](https://openreview.net/forum?id=ye4ntB1Kzi), [code](https://github.com/Thinklab-SJTU/ML4CO-Bench-101)
    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

35. **MeLA: A Metacognitive LLM-Driven Architecture for Automatic Heuristic Design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2507.20541), [code](https://github.com/Qzs1335/MeLA)

36. **Learn to Relax with Large Language Models: Solving Nonlinear Combinatorial Optimization Problems via Bidirectional Coevolution** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.12643)

37. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://neurips.cc/virtual/2025/loc/san-diego/poster/115835), [code](https://github.com/Summer142857/LLMCoSolver)
    *Xia Jiang, Yaoxin Wu, Minshuo Li, Zhiguang Cao, Yingqian Zhang*

38. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://arxiv.org/pdf/2509.16865), [code](https://github.com/Summer142857/LLMCoSolver)

39. **LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.14138)

40. **HIFO-PROMPT: Prompting with Hindsight and Foresight For LLM-Based Automatic Heuristic Design** ICLR, 2025. [paper](https://arxiv.org/pdf/2508.13333)

41. **Hierarchical Representations for Cross-task Automated Heuristic Design using LLMs** Under Review, 2025. [paper](https://openreview.net/pdf?id=dgvx86qybJ)

42. **HeurAgenix: Leveraging LLMs for Solving Complex Combinatorial Optimization Challenges** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.15196), [code](https://github.com/microsoft/HeurAgenix)

43. **GraphThought: Graph Combinatorial Optimization with Thought Generation** Arxiv, 2025. [paper](https://arxiv.org/pdf/2502.11607)

44. **GraphArena: Evaluating and Exploring Large Language Models on Graph Computation** ICLR, 2025. [paper](https://openreview.net/pdf?id=Y1r9yCMzeA), [code](https://github.com/squareRoot3/GraphArena/tree/master)

45. **Fusing LLMs with Scientific Literature for Heuristic Discovery** Under Review, 2025. [paper](https://openreview.net/pdf?id=lwqeXDYKWJ)

46. **Fitness Landscape of Large Language Model-Assisted Automated Algorithm Search** Arxiv, 2025. [paper](https://arxiv.org/pdf/2504.19636)

47. **Fine-tuning Large Language Model for Automated Algorithm Design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2507.10614)

48. **Experience-guided reflective co-evolution of prompts and heuristics for automatic algorithm design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.24509)

49. **Experience-Guided Reflective Co-Evolution of Prompts and Heuristics for Automatic Algorithm Design** Under Review, 2025. [paper](https://openreview.net/pdf?id=oD9RwlFqEE)

50. **Efficient Heuristics Generation for Solving Combinatorial Optimization Problems Using Large Language Models** KDD, 2025. [paper](https://arxiv.org/pdf/2505.12627v1), [code](https://github.com/wuuu110/Hercules)

51. **Efficient and Robust Neural Combinatorial Optimization via Wasserstein-Based Coresets** ICLR, 2025. [paper](https://openreview.net/forum?id=F57HPKZ6KD)
    *Xu Wang, Fuyou Miao, Wenjie Liu, Yan Xiong*

52. **EALG: Evolutionary Adversarial Generation of Language Model–Guided Generators for Combinatorial Optimization** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.02594)

53. **Combinatorial Optimization for All: Using LLMs to Aid Non-Experts in Improving Optimization Algorithms** Arxiv, 2025. [paper](https://arxiv.org/pdf/2503.10968), [code](https://github.com/camilochs/comb-opt-for-all)

54. **Cognitively Inspired Reflective Evolution: Interactive Multi-Turn LLM–EA Synthesis of Heuristics for Combinatorial Optimization** Under Review, 2025. [paper](https://openreview.net/pdf?id=31VTD5pS2v)

55. **CogMCTS: A Novel Cognitive-Guided Monte Carlo Tree Search Framework for Iterative Heuristic Evolution with Large Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.08609)

56. **COExpander: Adaptive Solution Expansion for Combinatorial Optimization** ICML, 2025. [paper](https://openreview.net/forum?id=KMaBXMWsBM), [code](https://github.com/Thinklab-SJTU/COExpander)
    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

57. **Code Evolution Graphs: Understanding Large Language Model Driven Design of Algorithms** GECCO, 2025. [paper](https://arxiv.org/pdf/2503.16668)

58. **CALM: Co-evolution of Algorithms and Language Model for Automatic Heuristic Design** ICLR, 2025. [paper](https://arxiv.org/pdf/2505.12285v1)

59. **Boosting Neural Combinatorial Optimization for Large-Scale Vehicle Routing Problems** ICLR, 2025. [paper](https://openreview.net/forum?id=TbTJJNjumY)
    *Fu Luo, Xi Lin, Yaoxin Wu, Zhenkun Wang, Tong Xialiang, Mingxuan Yuan, Qingfu Zhang*

60. **AutoMOAE: Multi-Objective Auto-Algorithm Evolution** Under Review, 2025. [paper](https://openreview.net/pdf?id=G8tP1Z9dLy)

61. **AutoEP: LLMs-Driven Automation of Hyperparameter Evolution for Metaheuristic Algorithms** ICLR, 2025. [paper](https://arxiv.org/pdf/2509.23189)

62. **Aligning LLMs with Graph Neural Solvers for Combinatorial Optimization** Under Review, 2025. [paper](https://openreview.net/pdf?id=KSfLDk3jxI)

63. **Algorithm Discovery With LLMs: Evolutionary Search Meets Reinforcement Learning** COLM, 2025. [paper](https://arxiv.org/pdf/2504.05108)

64. **ACCORD: Autoregressive Constraint-satisfying Generation for COmbinatorial Optimization with Routing and Dynamic attention** Under Review, 2025. [paper](https://openreview.net/pdf?id=f0TBAdcJ8m)

65. **A Comprehensive Evaluation of Contemporary ML-Based Solvers for Combinatorial Optimization** ICML 2025 Workshop AI4Math, 2025. [paper](https://arxiv.org/pdf/2505.16952), [code](https://huggingface.co/datasets/CO-Bench/FrontierCO)

66. **Visual Reasoning and Multi-Agent Approach in Multimodal Large Language Models (MLLMs): Solving TSP and mTSP Combinatorial Challenges** Arxiv, 2024. [paper](https://arxiv.org/pdf/2407.00092), [code](https://github.com/ahmed-abdulhuy/Solving-TSP-and-mTSP-Combinatorial-Challenges-using-Visual-Reasoning-and-Multi-Agent-Approach-MLLMs-)

67. **Unifying All Species: LLM-based Hyper-Heuristics for Multi-objective Optimization** Under Review, 2024. [paper](https://openreview.net/forum?id=sUywd7UhFT)

68. **UNCO: Towards Unifying Neural Combinatorial Optimization through Large Language Model** Arxiv, 2024. [paper](https://arxiv.org/pdf/2408.12214)

69. **UDC: A Unified Neural Divide-and-Conquer Framework for Large-Scale Combinatorial Optimization Problems** NeurIPS, 2024. [paper](https://openreview.net/pdf?id=dCgbyvmlwL), [code](https://github.com/CIAM-Group/NCO_code/tree/main/single_objective/UDC-Large-scale-CO-master)
    *Zhi Zheng, Changliang Zhou, Tong Xialiang, Mingxuan Yuan, Zhenkun Wang*

70. **Towards a Generic Representation of Combinatorial Problems for Learning-Based Approaches** CPAIOR, 2024. [paper](https://arxiv.org/pdf/2403.06026), [code](https://github.com/corail-research/learning-generic-csp)

71. **Toward Learning Generalized Cross-Problem Solving Strategies for Combinatorial Optimization** Under Review, 2024. [paper](https://openreview.net/forum?id=VnaJNW80pN)

72. **Solving Diverse Combinatorial Optimization Problems with a Unified Model** Under Review, 2024. [paper](https://openreview.net/forum?id=Kc3yoIL5oR)

73. **Self-Guiding Exploration for Combinatorial Problems** NeurIPS, 2024. [paper](https://arxiv.org/pdf/2405.17950), [code](https://github.com/Zangir/LLM-for-CP)

74. **ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution** NeurIPS, 2024. [paper](https://arxiv.org/pdf/2402.01145), [code](https://github.com/ai4co/reevo)

75. **QUBE: Enhancing Automatic Heuristic Design via Quality-Uncertainty Balanced Evolution** Arxiv, 2024. [paper](https://arxiv.org/pdf/2412.20694), [code](https://github.com/zzjchen/QUBE_code)

76. **Position: Rethinking Post-Hoc Search-Based Neural Approaches for Solving Large-Scale Traveling Salesman Problems** ICML, 2024. [paper](https://arxiv.org/abs/2406.03503), [code](https://github.com/xyfffff/rethink_mcts_for_tsp)
    *Yifan Xia, Xianliang Yang, Zichuan Liu, Zhihao Liu, Lei Song, Jiang Bian*

77. **Neural Combinatorial Optimization for Robust Routing Problem with Uncertain Travel Times** NeurIPS, 2024. [paper](https://openreview.net/pdf?id=DoewNm2uT3)
    *Pei Xiao, Zizhen Zhang, Jinbiao Chen, Jiahai Wang, Zhenzhen Zhang*

78. **Multi-objective Evolution of Heuristic Using Large Language Model** AAAI, 2024. [paper](https://arxiv.org/pdf/2409.16867)

79. **MARCO: A Memory-Augmented Reinforcement Framework for Combinatorial Optimization** IJCAI, 2024. [paper](https://www.ijcai.org/proceedings/2024/0766.pdf), [code](https://github.com/TheLeprechaun25/MARCO)
    *Andoni I. Garmendia, Quentin Cappart, Josu Ceberio, Alexander Mendiburu*

80. **Learning to Handle Complex Constraints for Vehicle Routing Problems** NeurIPS, 2024. [paper](https://openreview.net/forum?id=Ktx95ZuRjP)
    *Jieyi Bi, Yining Ma, Jianan Zhou, Wen Song, Zhiguang Cao, Yaoxin Wu, Jie Zhang*

81. **HSEvo: Elevating Automatic Heuristic Design with Diversity-Driven Harmony Search and Genetic Algorithm Using LLMs** AAAI, 2024. [paper](https://arxiv.org/pdf/2412.14995), [code](https://github.com/datphamvn/HSEvo)

82. **GOAL: A Generalist Combinatorial Optimization Agent Learner** ICLR, 2024. [paper](https://arxiv.org/pdf/2406.15079), [code](https://github.com/naver/goal-co)

83. **GLOP: Learning Global Partition and Local Construction for Solving Large-Scale Routing Problems in Real-Time** AAAI, 2024. [paper](https://arxiv.org/abs/2312.08224), [code](https://github.com/henry-yeh/GLOP)
    *Haoran Ye, Jiarui Wang, Helan Liang, Zhiguang Cao, Yong Li, Fanzhang Li*

84. **Fast T2T: Optimization Consistency Speeds Up Diffusion-Based Training-to-Testing Solving for Combinatorial Optimization** NeurIPS, 2024. [paper](https://openreview.net/pdf?id=xDrKZOZEOc), [code](https://github.com/Thinklab-SJTU/Fast-T2T)
    *Yang Li, Jinpei Guo, Runzhong Wang, Hongyuan Zha, Junchi Yan*

85. **Eyeballing Combinatorial Problems: A Case Study of Using Multimodal Large Language Models to Solve Traveling Salesman Problems** ISBCom, 2024. [paper](https://arxiv.org/pdf/2406.06865)

86. **Evolution of Heuristics: Towards Efficient Automatic Algorithm Design Using Large Language Model** ICML, 2024. [paper](https://arxiv.org/pdf/2401.02051), [code](https://github.com/FeiLiu36/EoH)

87. **Distilling Autoregressive Models to Obtain High-Performance Non-autoregressive Solvers for Vehicle Routing Problems with Faster Inference Speed** AAAI, 2024. [paper](https://arxiv.org/abs/2312.12469), [code](https://github.com/xybFight/GNARKD)
    *Yubin Xiao, Di Wang, Boyang Li, Mingzhao Wang, Xuan Wu, Changliang Zhou, You Zhou*

88. **Cross-Problem Learning for Solving Vehicle Routing Problems** IJCAI, 2024. [paper](https://arxiv.org/pdf/2404.11677), [code](https://github.com/Zhuoyi-Lin/Cross_problem_learning)

89. **Collaboration! Towards Robust Neural Methods for Routing Problems** NeurIPS, 2024. [paper](https://openreview.net/forum?id=YfQA78gEFA), [code](https://github.com/RoyalSkye/Routing-CNF)
    *Jianan Zhou, Yaoxin Wu, Zhiguang Cao, Wen Song, Jie Zhang, Zhiqi Shen*

90. **Can Large Language Models Solve Robot Routing?** Arxiv, 2024. [paper](https://arxiv.org/pdf/2403.10795), [code](https://github.com/Zhehui-Huang/LLM_Routing)

91. **Winner Takes It All: Training Performant RL Populations for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=v6VpqGcGAR)
    *Nathan Grinsztajn, Daniel Furelos-Blanco, Shikha Surana, Cl{\'e}ment Bonnet, Thomas D Barrett*

92. **Unsupervised Learning for Solving the Travelling Salesman Problem** NeurIPS, 2023. [paper](https://openreview.net/forum?id=lAEc7aIW20)
    *Yimeng Min, Yiwei Bai, Carla P Gomes*

93. **Towards Omni-generalizable Neural Methods for Vehicle Routing Problems** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25267), [code](https://github.com/RoyalSkye/Omni-VRP)
    *Zhou Jianan, Yaoxin Wu, Wen Song, Zhiguang Cao, Jie Zhang*

94. **T2T: From Distribution Learning in Training to Gradient Search in Testing for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=JtF0ugNMv2), [code](https://github.com/Thinklab-SJTU/T2TCO)
    *Yang Li, Jinpei Guo, Runzhong Wang, Junchi Yan*

95. **Select and Optimize: Learning to solve large-scale TSP instances** AISTATS, 2023. [paper](https://proceedings.mlr.press/v206/cheng23a.html)
    *Hanni Cheng, Haosi Zheng, Ya Cong, Weihao Jiang, Shiliang Pu*

96. **ROCO: A General Framework for Evaluating Robustness of Combinatorial Optimization Solvers on Graphs** ICLR, 2023. [paper](https://openreview.net/forum?id=2r6YMqz4Mml), [code](https://github.com/Thinklab-SJTU/ROCO)
    *Han Lu, Zenan Li, Runzhong Wang, Qibing Ren, Xijun Li, Mingxuan Yuan, Jia Zeng, Xiaokang Yang, Junchi Yan*

97. **Revisiting Sampling for Combinatorial Optimization** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/23661)
    *Haoran, Goshvadi Katayoon, Nova Azade, Schuurmans Dale Sun, Dai Hanjun.*

98. **Reinforced Lin–Kernighan–Helsgaun Algorithms for the Traveling Salesman Problems** Knowledge-Based Systems, 2023. [paper](https://www.sciencedirect.com/science/article/pii/S0950705122012400), [code](https://github.com/JHL-HUST/VSR-LKH-V2)
    *Jiongzhi Zheng, Kun He, Jianrong Zhou, Yan Jin, Chu-Min Li*

99. **Pointerformer: Deep Reinforced Multi-Pointer Transformer for the Traveling Salesman Problem** Arxiv, 2023. [paper](https://arxiv.org/abs/2304.09407), [code](https://github.com/Pointerformer/Pointerformer)
    *Yan Jin, Yuandong Ding, Xuanhao Pan, Kun He, Li Zhao, Tao Qin, Lei Song, Jiang Bian*

100. **Optimizing Solution-Samplers for Combinatorial Problems: The Landscape of Policy-Gradient Methods** NeurIPS, 2023. [paper](https://openreview.net/forum?id=mmTy1iyU5G), [code](https://openreview.net/attachment?id=mmTy1iyU5G&name=supplementary_material)
    *Constantine Caramanis, Dimitris Fotakis, Alkis Kalavasis, Vasilis Kontonis, Christos Tzamos*

101. **NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes** ACL, 2023. [paper](https://arxiv.org/pdf/2312.14890), [code](https://github.com/casmlab/NPHardEval)

102. **Neural Multi-Objective Combinatorial Optimization with Diversity Enhancement** NeurIPS, 2023. [paper](https://openreview.net/forum?id=N4JkStI1fe), [code](https://github.com/bill-cjb/NHDE)
    *Jinbiao Chen, Zizhen Zhang, Zhiguang Cao, Yaoxin Wu, Yining Ma, Te Ye, Jiahai Wang*

103. **Neural Improvement Heuristics for Graph Combinatorial Optimization Problems** TNNLS, 2023. [paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10271315&casa_token=Hqn_wH2HAjEAAAAA:rTd6KVaoKVjrFWASa-Ma0vC6CBvsmMUHnoWik2DyD56NbnfNOqBG5qZTBLR5hqf9vpCotivB_BU&tag=1), [code](https://github.com/TheLeprechaun25/neural-improvement-heuristics)
    *Andoni I. Garmendia, Josu Ceberio, Alexander Mendiburu*

104. **Neural Combinatorial Optimization with Heavy Decoder: Toward Large Scale Generalization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=RBI4oAbdpm), [code](https://github.com/CIAM-Group/NCO_code/tree/main/single_objective/LEHD)
    *Fu Luo, Xi Lin, Fei Liu, Qingfu Zhang, Zhenkun Wang*

105. **Multi-View Graph Contrastive Learning for Solving Vehicle Routing Problems** UAI, 2023. [paper](https://openreview.net/pdf?id=Z-mRKVaxVU3)
    *Yuan Jiang, Zhiguang Cao, Yaoxin Wu, Jie Zhang*

106. **Meta-SAGE: Scale Meta-Learning Scheduled Adaptation with Guided Exploration for Mitigating Scale Shift on Combinatorial Optimization** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25138)
    *Jiwoo Son, Minsu Kim, Hyeonah Kim, Jinkyoo Park*

107. **LinSATNet: The Positive Linear Satisfiability Neural Networks** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25110), [code](https://github.com/Thinklab-SJTU/LinSATNet)
    *Runzhong Wang, Yunhao Zhang, Ziao Guo, Tianyi Chen, Xiaokang Yang, Junchi Yan*

108. **Learning to Search Feasible and Infeasible Regions of Routing Problems with Flexible Neural k-Opt** NeurIPS, 2023. [paper](https://openreview.net/forum?id=q1JukwH2yP), [code](https://github.com/yining043/NeuOpt)
    *Yining Ma, Zhiguang Cao, Yeow Meng Chee*

109. **Learning to CROSS exchange to solve min-max vehicle routing problems** ICLR, 2023. [paper](https://openreview.net/forum?id=ZcnzsHC10Y)
    *Minjun Kim, Junyoung Park, Jinkyoo Park*

110. **Large Language Models as Optimizers** ICLR, 2023. [paper](https://arxiv.org/pdf/2309.03409), [code](https://github.com/google-deepmind/opro)

111. **Large Language Models as Evolutionary Optimizers** CEC, 2023. [paper](https://arxiv.org/pdf/2310.19046), [code](https://github.com/cschen1205/LMEA)

112. **H-tsp: Hierarchically solving the large-scale traveling salesman problem** AAAI, 2023. [paper](https://www.microsoft.com/en-us/research/publication/h-tsp-hierarchically-solving-the-large-scale-traveling-salesman-problem/), [code](https://github.com/Learning4Optimization-HUST/H-TSP)
    *Xuanhao Pan, Yan Jin, Yuandong Ding, Mingxiao Feng, Li Zhao, Lei Song, Jiang Bian*

113. **Generalize Learned Heuristics to Solve Large-scale Vehicle Routing Problems in Real-time** ICLR, 2023. [paper](https://openreview.net/forum?id=6ZajpxqTlQ)
    *Qingchun Hou, Jingwei Yang, Yiqiang Su, Xiaoqing Wang, Yuming Deng*

114. **Ensemble-based Deep Reinforcement Learning for Vehicle Routing Problems under Distribution Shift** NeurIPS, 2023. [paper](https://openreview.net/forum?id=HoBbZ1vPAh)
    *Yuan Jiang, Zhiguang Cao, Yaoxin Wu, Wen Song, Jie Zhang*

115. **Efficient Training of Multi-task Combinatorial Neural Solver with Multi-armed Bandits** TMLR, 2023. [paper](https://arxiv.org/pdf/2305.06361)

116. **Efficient Meta Neural Heuristic for Multi-Objective Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=593fc38lhN), [code](https://github.com/bill-cjb/EMNH)
    *Jinbiao Chen, Jiahai Wang, Zizhen Zhang, Zhiguang Cao, Te Ye, Siyuan Chen*

117. **DIFUSCO: Graph-based Diffusion Solvers for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=JV8Ff0lgVV), [code](https://github.com/Edward-Sun/DIFUSCO)
    *Zhiqing Sun, Yiming Yang*

118. **DeepACO: Neural-enhanced Ant Systems for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=cd5D1DD923), [code](https://github.com/henry-yeh/DeepACO)
    *Haoran Ye, Jiarui Wang, Zhiguang Cao, Helan Liang, Yong Li*

119. **Combinatorial Optimization with Policy Adaptation using Latent Space Search** NeurIPS, 2023. [paper](https://openreview.net/forum?id=vpMBqdt9Hl)
    *Felix Chalumeau, Shikha Surana, Cl{\'e}ment Bonnet, Nathan Grinsztajn, Arnu Pretorius, Alexandre Laterre, Thomas D Barrett*

120. **BQ-NCO: Bisimulation Quotienting for Efficient Neural Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=BRqlkTDvvm), [code](https://github.com/naver/bq-nco)
    *Darko Drakulic, Sofia Michel, Florian Mai, Arnaud Sors, Jean-Marc Andreoli*

121. **Algorithm Evolution Using Large Language Model** Arxiv, 2023. [paper](https://arxiv.org/pdf/2311.15249)

122. **The First AI4TSP Competition: Learning to Solve Stochastic Routing Problems** Arxiv, 2022. [paper](https://arxiv.org/abs/2201.10453), [code](https://github.com/paulorocosta/ai-for-tsp-competition)
    *Laurens Bliek, Paulo da Costa, Reza Refaei Afshar, Yingqian Zhang, Tom Catshoek, Daniel Vos, Sicco Verwer, Fynn Schmitt-Ulms, Andre Hottung, Tapan Shah, others*

123. **Sym-NCO: Leveraging Symmetricity for Neural Combinatorial Optimization** NeurIPS, 2022. [paper](https://openreview.net/forum?id=kHrE2vi5Rvs), [code](https://github.com/alstn12088/Sym-NCO)
    *Minsu Kim, Junyoung Park, Jinkyoo Park*

124. **Simulation-guided Beam Search for Neural Combinatorial Optimization** NeurIPS, 2022. [paper](https://openreview.net/forum?id=tYAS1Rpys5), [code](https://github.com/yd-kwon/SGBS)
    *Jinho Choo, Yeong-Dae Kwon, Jihoon Kim, Jeongwoo Jae, Andr{\'e} Hottung, Kevin Tierney, Youngjune Gwon*

125. **Preference Conditioned Neural Multi-objective Combinatorial Optimization** ICLR, 2022. [paper](https://openreview.net/forum?id=QuObT9BTWo)
    *Xi Lin, Zhiyuan Yang, Qingfu Zhang*

126. **Learning Generalizable Models for Vehicle Routing Problems via Knowledge Distillation** NeurIPS, 2022. [paper](https://openreview.net/forum?id=sOVNpUEgKMp), [code](https://github.com/jieyibi/AMDKD)
    *Jieyi Bi, Yining Ma, Jiahai Wang, Zhiguang Cao, Jinbiao Chen, Yuan Sun, Yeow Meng Chee*

127. **Graph Neural Network Guided Local Search for the Traveling Salesperson Problem** ICLR, 2022. [paper](https://openreview.net/forum?id=ar92oEosBIg)
    *Benjamin Hudson, Qingbiao Li, Matthew Malencia, Amanda Prorok*

128. **Generalization of Neural Combinatorial Solvers Through the Lens of Adversarial Robustness** ICLR, 2022. [paper](https://openreview.net/forum?id=vJZ7dPIjip3)
    *Simon Geisler, Johanna Sommer, Jan Schuchardt, Aleksandar Bojchevski, Stephan Günnemann*

129. **DIMES: A Differentiable Meta Solver for Combinatorial Optimization Problems** NeurIPS, 2022. [paper](https://openreview.net/forum?id=9u05zr0nhx)
    *Ruizhong Qiu, Zhiqing Sun, Yiming Yang*

130. **The Transformer Network for the Traveling Salesman Problem** IPAM, 2021. [paper](http://helper.ipam.ucla.edu/publications/dlc2021/dlc2021_16703.pdf)
    *Xavier Bresson，Thomas Laurent*

131. **Solving Dynamic Traveling Salesman Problems with Deep Reinforcement Learning.** TNNLS, 2021. [paper](https://ieeexplore.ieee.org/document/9537638)
    *Zizhen Zhang, Hong Liu, Meng Chu Zhou, Jiahai Wang*

132. **ScheduleNet: Learn to Solve Multi-agent Scheduling Problems with Reinforcement Learning** Arxiv, 2021. [paper](https://arxiv.org/abs/2106.03051)
    *Junyoung Park, Sanjar Bakhtiyar, Jinkyoo Park*

133. **Reversible Action Design for Combinatorial Optimization with Reinforcement Learning** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.07210)
    *Fan Yao, Renqin Cai, Hongning Wang*

134. **Reinforcement Learning for Route Optimization with Robustness Guarantees** IJCAI, 2021. [paper](https://www.ijcai.org/proceedings/2021/0357.pdf)
    *Tobias Jacobs, Francesco Alesiani, Gulcin Ermis*

135. **Learning TSP Requires Rethinking Generalization** CP, 2021. [paper](https://arxiv.org/pdf/2006.07054.pdf), [code](https://github.com/chaitjo/learning-tsp)
    *Chaitanya K. Joshi, Quentin Cappart, Louis-Martin Rousseau, Thomas Laurent*

136. **Learning to Sparsify Travelling Salesman Problem Instances** CPAIOR, 2021. [paper](https://dx.doi.org/10.1007/978-3-030-78230-6_26)
    *James Fitzpatrick, Deepak Ajwani, Paula Carroll*

137. **Learning Improvement Heuristics for Solving Routing Problems** TNNLS, 2021. [paper](https://ieeexplore.ieee.org/abstract/document/9393606?casa_token=mFeyLmrOGfIAAAAA:nmAkjUaTSooYurWHuWGYNoguV453anw9Enyv45xG5jb2oCps6QE4A1CFe1EmFmTzbON6cL5maw)
    *Yaoxin Wu, Wen Song, Zhiguang Cao, Jie Zhang, Andrew Lim*

138. **Deep Reinforcement Learning for Combinatorial Optimization: Covering Salesman Problems.** IEEE Trans Cybern, 2021. [paper](https://arxiv.org/abs/2102.05875)
    *Kaiwen Li, Tao Zhang, Rui Wang Yuheng Wang, Yi Han*

139. **DAN: Decentralized Attention-based Neural Network to Solve the MinMax Multiple Traveling Salesman Problem** Arxiv, 2021. [paper](https://arxiv.org/abs/2109.04205)
    *Yuhong Cao, Zhanhong Sun, Guillaume Sartoretti*

140. **Combining Reinforcement Learning with Lin-Kernighan-Helsgaun Algorithm for the Traveling Salesman Problem** AAAI, 2021. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/17476/17283), [code](https://github.com/JHL-HUST/VSR-LKH-V2)
    *Jiongzhi Zheng, Kun He, Jianrong Zhou, Yan Jin, Chu-Min Li*

141. **POMO: Policy Optimization with Multiple Optima for Reinforcement Learning.** NeurIPS, 2020. [paper](https://arxiv.org/abs/2010.16011), [code](https://github.com/yd-kwon/POMO/)
    *Yeong-Dae Kwon, Jinho Choo, Byoungjip Kim, Iljoo Yoon, Seungjai Min, Youngjune Gwon*

142. **Learning 2-opt Heuristics for the Traveling Salesman Problem via Deep Reinforcement Learning** ACML, 2020. [paper](http://proceedings.mlr.press/v129/costa20a), [code](https://github.com/paulorocosta/learning-2opt-drl)
    *d O Costa, Paulo R, Jason Rhuggenaath, Yingqian Zhang, Alp Akcay*

143. **Generalize a Small Pre-trained Model to Arbitrarily Large TSP Instances.** Arxiv, 2020. [paper](https://arxiv.org/abs/2012.10658)
    *Zhang-Hua Fu, Kai-Bin Qiu, Hongyuan Zha*

144. **A Reinforcement Learning Approach for Optimizing Multiple Traveling Salesman Problems over Graphs** KBS, 2020. [paper](https://www.sciencedirect.com/science/article/pii/S0950705120304445)
    *Yujiao Hu, Yuan Yao, Wee Sun Lee*

145. **Learning to Solve NP-Complete Problems: A Graph Neural Network for Decision TSP.** AAAI, 2019. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/4399)
    *Marcelo Prates, Pedro HC Avelar, Henrique Lemos, Luis C Lamb, Moshe Y. Vardi*

146. **Attention, Learn to Solve Routing Problems!** ICLR, 2019. [paper](https://arxiv.org/abs/1803.08475)
    *Wouter Kool, Herke Van Hoof, Max Welling*

147. **An Efficient Graph Convolutional Network Technique for the Travelling Salesman Problem** Arxiv, 2019. [paper](https://arxiv.org/abs/1906.01227), [code](https://github.com/chaitjo/graph-convnet-tsp)
    *Chaitanya K. Joshi, Thomas Laurent, Xavier Bresson*

148. **Learning Heuristics for the TSP by Policy Gradient** CPAIOR, 2018. [paper](https://link.springer.com/chapter/10.1007/978-3-319-93031-2_12), [code](https://github.com/MichelDeudon/encode-attend-navigate)
    *Michel DeudonPierre CournutAlexandre Lacoste*

149. **Learning Combinatorial Optimization Algorithms over Graphs.** NeurIPS, 2017. [paper](https://arxiv.org/abs/1704.01665)
    *Hanjun Dai, Elias B Khalil, Yuyu Zhang, Bistra Dilkina, Le Song*

### [Portfolio Optimization](#content) · *3 papers*

1. **Towards One-shot Neural Combinatorial Solvers: Theoretical and Empirical Notes on the Cardinality-Constrained Case** ICLR, 2023. [paper](https://openreview.net/forum?id=h21yJhdzbwz), [code](https://github.com/Thinklab-SJTU/One-Shot-Cardinality-NN-Solver)
    *Runzhong Wang, Li Shen, Yiting Chen, Junchi Yan, Xiaokang Yang, Dacheng Tao*

2. **LinSATNet: The Positive Linear Satisfiability Neural Networks** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25110), [code](https://github.com/Thinklab-SJTU/LinSATNet)
    *Runzhong Wang, Yunhao Zhang, Ziao Guo, Tianyi Chen, Xiaokang Yang, Junchi Yan*

3. **Integrating prediction in mean-variance portfolio optimization** Quantitative Finance, 2023. [paper](https://arxiv.org/pdf/2102.09287.pdf)
    *Andrew Butler, Roy H Kwon*

### [Maximal Cut](#content) · *22 papers*

1. **Scalable Discrete Diffusion Samplers: Combinatorial Optimization and Statistical Physics** ICLR, 2025. [paper](https://openreview.net/pdf?id=peNgxpbdxB)
    *Sebastian Sanokowski, Wilhelm Franz Berghammer, Haoyu Peter Wang, Martin Ennemoser, Sepp Hochreiter, Sebastian Lehner*

2. **ML4CO-Bench-101: Benchmark Machine Learning for Classic Combinatorial Problems on Graphs** NeurIPS, 2025. [paper](https://openreview.net/forum?id=ye4ntB1Kzi), [code](https://github.com/Thinklab-SJTU/ML4CO-Bench-101)
    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

3. **Learning to Explore and Exploit with GNNs for Unsupervised Combinatorial Optimization** ICLR, 2025. [paper](https://openreview.net/forum?id=vaJ4FObpXN), [code](https://github.com/utkuumur/X2GNN)
    *Utku Umur Acikalin, Aaron M. Ferber, Carla P. Gomes*

4. **HeurAgenix: Leveraging LLMs for Solving Complex Combinatorial Optimization Challenges** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.15196), [code](https://github.com/microsoft/HeurAgenix)

5. **COExpander: Adaptive Solution Expansion for Combinatorial Optimization** ICML, 2025. [paper](https://openreview.net/forum?id=KMaBXMWsBM), [code](https://github.com/Thinklab-SJTU/COExpander)
    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

6. **MARCO: A Memory-Augmented Reinforcement Framework for Combinatorial Optimization** IJCAI, 2024. [paper](https://www.ijcai.org/proceedings/2024/0766.pdf), [code](https://github.com/TheLeprechaun25/MARCO)
    *Andoni I. Garmendia, Quentin Cappart, Josu Ceberio, Alexander Mendiburu*

7. **Efficient Combinatorial Optimization via Heat Diffusion** NeurIPS, 2024. [paper](https://openreview.net/forum?id=psDrko9v1D), [code](https://github.com/AwakerMhy/HeO)
    *Hengyuan Ma, Wenlian Lu, Jianfeng Feng*

8. **Distributed Constrained Combinatorial Optimization leveraging Hypergraph Neural Networks** Nature Machine Intelligence, 2024. [paper](https://arxiv.org/abs/2311.09375), [code](https://github.com/nasheydari/HypOp)
    *Nasimeh Heydaribeni, Xinrui Zhan, Ruisi Zhang, Tina Eliassi-Rad, Farinaz Koushanfar*

9. **Controlling Continuous Relaxation for Combinatorial Optimization** NeurlPS, 2024. [paper](https://openreview.net/pdf?id=ykACV1IhjD)
    *Yuma Ichikawa*

10. **A Diffusion Model Framework for Unsupervised Neural Combinatorial Optimization** ICML, 2024. [paper](https://arxiv.org/abs/2406.01661), [code](https://github.com/ml-jku/DIffUCO)
    *Sebastian Sanokowski, Sepp Hochreiter, Sebastian Lehner*

11. **Variational Annealing on Graphs for Combinatorial Optimization** NeurlPS, 2023. [paper](https://openreview.net/forum?id=SLx7paoaTU), [code](https://github.com/ml-jku/VAG-CO)
    *Sebastian Sanokowski, Wilhelm Franz Berghammer, Sepp Hochreiter, Sebastian Lehner*

12. **Revisiting Sampling for Combinatorial Optimization** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/23661)
    *Haoran, Goshvadi Katayoon, Nova Azade, Schuurmans Dale Sun, Dai Hanjun.*

13. **Optimizing Solution-Samplers for Combinatorial Problems: The Landscape of Policy-Gradient Methods** NeurIPS, 2023. [paper](https://openreview.net/forum?id=mmTy1iyU5G), [code](https://openreview.net/attachment?id=mmTy1iyU5G&name=supplementary_material)
    *Constantine Caramanis, Dimitris Fotakis, Alkis Kalavasis, Vasilis Kontonis, Christos Tzamos*

14. **Neural Improvement Heuristics for Graph Combinatorial Optimization Problems** TNNLS, 2023. [paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10271315&casa_token=Hqn_wH2HAjEAAAAA:rTd6KVaoKVjrFWASa-Ma0vC6CBvsmMUHnoWik2DyD56NbnfNOqBG5qZTBLR5hqf9vpCotivB_BU&tag=1), [code](https://github.com/TheLeprechaun25/neural-improvement-heuristics)
    *Andoni I. Garmendia, Josu Ceberio, Alexander Mendiburu*

15. **Let the Flows Tell: Solving Graph Combinatorial Optimization Problems with GFlowNets** NeurlPS, 2023. [paper](https://arxiv.org/abs/2305.17010), [code](https://github.com/zdhNarsil/GFlowNet-CombOpt)
    *Dinghuai Zhang, Hanjun Dai, Nikolay Malkin, Aaron Courville, Yoshua Bengio, Ling Pan*

16. **DISCS: A Benchmark for Discrete Sampling** NeurlPS, 2023. [paper](https://openreview.net/forum?id=oi1MUMk5NF), [code](https://github.com/google-research/discs)
    *Katayoon Goshvadi, Haoran Sun, Xingchao Liu, Azade Nova, Ruqi Zhang, Will Sussman Grathwohl, Dale Schuurmans, Hanjun Dai*

17. **LeNSE: Learning To Navigate Subgraph Embeddings for Large-Scale Combinatorial Optimisation** ICML, 2022. [paper](https://proceedings.mlr.press/v162/ireland22a.html), [code](https://github.com/davidireland3/LeNSE)
    *David Ireland, G. Montana*

18. **Learning to Solve Combinatorial Graph Partitioning Problems via Efficient Exploration** Arxiv, 2022. [paper](https://arxiv.org/abs/2205.14105), [code](https://github.com/tomdbar/ecord)
    *Thomas D Barrett, Christopher WF Parsonson, Alexandre Laterre*

19. **Reversible Action Design for Combinatorial Optimization with Reinforcement Learning** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.07210)
    *Fan Yao, Renqin Cai, Hongning Wang*

20. **Exploratory Combinatorial Optimization with Reinforcement Learning.** AAAI, 2020. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/5723)
    *Thomas LBarrett, William Clements, Jakob Foerster, Alex Lvovsky*

21. **Erdos Goes Neural: an Unsupervised Learning Framework for Combinatorial Optimization on Graphs.** NeurIPS, 2020. [paper](https://static.aminer.cn/upload/pdf/575/1127/1864/5eede0b791e0116a23aafe7b_1.pdf)
    *Nikolaos Karalias, Andreas Loukas*

22. **Learning Combinatorial Optimization Algorithms over Graphs.** NeurIPS, 2017. [paper](https://arxiv.org/abs/1704.01665)
    *Hanjun Dai, Elias B Khalil, Yuyu Zhang, Bistra Dilkina, Le Song*

### [Vehicle Routing Problem](#content) · *113 papers*

1. **Towards Efficient Constraint Handling in Neural Solvers for Routing Problems** ICLR, 2026. [paper](https://openreview.net/forum?id=raDFGuQxvD), [code](https://github.com/jieyibi/CaR-constraint)
    *Jieyi Bi, Zhiguang Cao, Jianan Zhou, Wen Song, Yaoxin Wu, Jie Zhang, Yining Ma, Cathy Wu*

2. **RRNCO: Towards Real-World Routing with Neural Combinatorial Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2503.16159), [code](https://github.com/ai4co/real-routing-nco)
    *Jiwoo Son, Zhikai Zhao, Federico Berto, Chuanbo Hua, Zhiguang Cao, Changhyun Kwon, Jinkyoo Park*

3. **Rethinking LLM-Driven Heuristic Design: Generating Efficient and Specialized Solvers via Dynamics-Aware Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.20868)

4. **Refining Hybrid Genetic Search for CVRP via Reinforcement Learning-Finetuned LLM** ICLR, 2026. [paper](https://arxiv.org/abs/2510.11121), [code](https://github.com/zaodushi/RFTHGS)
    *Rongjie Zhu, Cong Zhang, Zhiguang Cao*

5. **RADAR: Learning to Route with Asymmetry-aware Distance Representations** ICLR, 2026. [paper](https://openreview.net/forum?id=lWdxX5s9T1), [code](https://github.com/yihang0410/RADAR)
    *Hang Yi, Ziwei Huang, Yining Ma, Zhiguang Cao*

6. **PathWise: Planning through World Model for Automated Heuristic Design via Self-Evolving LLMs** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.20539)

7. **Native Adaptive Solution Expansion for Diffusion-based Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=084SvT55yk)
    *Yu Wang, Yang Li, Jiale Ma, Junchi Yan, Yi Chang*

8. **Multi-Action Self-Improvement for Neural Combinatorial Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2510.12273), [code](https://github.com/LTluttmann/macsim)
    *Laurin Luttmann, Lin Xie*

9. **MaskCO: Masked Generation Drives Effective Representation Learning and Exploiting for Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=psUjNnLhl9), [code](https://github.com/Thinklab-SJTU/MaskCO)
    *Lvda Chen, Yang Li, Junchi Yan*

10. **Learning to Segment for Vehicle Routing Problems** ICLR, 2026. [paper](https://arxiv.org/abs/2507.01037), [code](https://github.com/mit-wu-lab/learning-to-segment)
    *Wenbin Ouyang, Sirui Li, Yining Ma, Cathy Wu*

11. **Heuristic Search as Language-Guided Program Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.16038)

12. **Hard Constraints Meet Soft Generation: Guaranteed Feasibility for LLM-based Combinatorial Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.01090)

13. **Generalizable Heuristic Generation Through LLMs with Meta-Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2505.20881), [code](https://github.com/yiding-s/MoH)
    *Yiding Shi, Jianan Zhou, Wen Song, Jieyi Bi, Yaoxin Wu, Zhiguang Cao, Jie Zhang*

14. **Game-Theoretic Co-Evolution for LLM-Based Heuristic Discovery** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.22896)

15. **G-LNS: Generative Large Neighborhood Search for LLM-Based Automatic Heuristic Design** Arxiv, 2026. [paper](https://arxiv.org/abs/2602.08253), [code](https://github.com/ZBoyn/G-LNS)
    *Baoyun Zhao, He Wang, Liang Zeng*

16. **EoH-S: Evolution of Heuristic Set using LLMs for Automated Heuristic Design** AAAI, 2026. [paper](https://arxiv.org/abs/2508.03082), [code](https://github.com/FeiLiu36/EoH-S)
    *Fei Liu, Yilu Liu, Qingfu Zhang, Xialiang Tong, Mingxuan Yuan*

17. **Enhancing CVRP Solver through LLM-driven Automatic Heuristic Design** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.23092)

18. **DyACE: Dynamic Algorithm Co-evolution for Online Automated Heuristic Design with Large Language Model** Arxiv, 2026. [paper](https://arxiv.org/pdf/2603.13344)

19. **DRAGON: LLM-Driven Decomposition and Reconstruction Agents for Large-Scale Combinatorial Optimization** AAMAS, 2026. [paper](https://arxiv.org/abs/2601.06502)
    *Shengkai Chen, Zhiguang Cao, Jianan Zhou, Yaoxin Wu, Senthilnath Jayavelu, Zhuoyi Lin, Xiaoli Li, Shili Xiang*

20. **Combination-of-Experts with Knowledge Sharing for Cross-Task Vehicle Routing Problems** ICLR, 2026. [paper](https://openreview.net/forum?id=lHBs9mbgwp), [code](https://github.com/yuzikang0/CoEKS)
    *Zikang Yu, Jinbiao Chen, Jiahai Wang*

21. **Chain-of-Context Learning: Dynamic Constraint Understanding for Multi-Task VRPs** ICLR, 2026. [paper](https://openreview.net/forum?id=AhE6aSlz5g), [code](https://github.com/gshuangchun/CCL-MTLVRP)
    *Shuangchun Gui, Suyu Liu, Xuehe Wang, Zhiguang Cao*

22. **Bridging Synthetic and Real Routing Problems via LLM-Guided Instance Generation and Progressive Adaptation** AAAI, 2026. [paper](https://arxiv.org/abs/2511.10233), [code](https://github.com/HenryZhu1029/EvoReal)
    *Jianghan Zhu, Yaoxin Wu, Zhuoyi Lin, Zhengyuan Zhang, Haiyan Yin, Zhiguang Cao, Senthilnath Jayavelu, Xiaoli Li*

23. **Beyond the Node: Clade-level Selection for Efficient MCTS in Automatic Heuristic Design** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.00549)

24. **Beyond Simple Graphs: Neural Multi-Objective Routing on Multigraphs** ICLR, 2026. [paper](https://arxiv.org/abs/2506.22095), [code](https://github.com/filiprydin/GMS)
    *Filip Rydin, Attila Lischka, Jiaming Wu, Morteza Haghir Chehreghani, Balazs Kulcsar*

25. **An Agentic Framework with LLMs for Solving Complex Vehicle Routing Problems** ICLR, 2026. [paper](https://openreview.net/forum?id=BMOgYw4EhQ), [code](https://github.com/ZHANG-NI/AFL)
    *Ni Zhang, Zhiguang Cao, Jianan Zhou, Cong Zhang, Yew-Soon Ong*

26. **VRPAgent: LLM-Driven Discovery of Heuristic Operators for Vehicle Routing Problems** Arxiv, 2025. [paper](https://arxiv.org/pdf/2510.07073), [code](https://github.com/ai4co/vrpagent)

27. **TPD-AHD: Textual Preference Differentiation for LLM-Based Automatic Heuristic Design** Under Review, 2025. [paper](https://openreview.net/pdf?id=VEMknlIPtM)

28. **RoCo: Role-Based LLMs Collaboration for Automatic Heuristic Design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.03762)

29. **Rethinking Neural Multi-Objective Combinatorial Optimization via Neat Weight Embedding** ICLR, 2025. [paper](https://openreview.net/forum?id=GM7cmQfk2F)
    *Jinbiao Chen, Zhiguang Cao, Jiahai Wang, Yaoxin Wu, Hanzhang Qin, Zizhen Zhang, Yue-Jiao Gong*

30. **RedAHD: Reduction-Based End-to-End Automatic Heuristic Design with Large Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2505.20242)

31. **Pareto-Grid-Guided Large Language Models for Fast and High-Quality Heuristics Design in Multi-Objective Combinatorial Optimization** AAAI, 2025. [paper](https://arxiv.org/pdf/2507.20923), [code](https://github.com/langkhachhoha/MPaGE)

32. **OptiHive: Ensemble Selection for LLM-Based Optimization via Statistical Modeling** Arxiv, 2025. [paper](https://arxiv.org/pdf/2508.02503)

33. **Nested-Refinement Metamorphosis: Reflective Evolution for Efficient Optimization of Networking Problems** ACL, 2025. [paper](https://aclanthology.org/2025.findings-acl.895.pdf)

34. **MOTIF: Multi-strategy Optimization via Turn-based Interactive Framework** AAAI, 2025. [paper](https://arxiv.org/abs/2508.03929), [code](https://github.com/HaiAu2501/MOTIF)

35. **Monte Carlo Tree Search for Comprehensive Exploration in LLM-Based Automatic Heuristic Design** ICML, 2025. [paper](https://arxiv.org/pdf/2501.08603), [code](https://github.com/zz1358m/MCTS-AHD-master)

36. **ML4CO-Bench-101: Benchmark Machine Learning for Classic Combinatorial Problems on Graphs** NeurIPS, 2025. [paper](https://openreview.net/forum?id=ye4ntB1Kzi), [code](https://github.com/Thinklab-SJTU/ML4CO-Bench-101)
    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

37. **LRM-1B: Towards Large Routing Model** Arxiv, 2025. [paper](https://www.arxiv.org/pdf/2507.03300)

38. **LLM-Driven Instance-Specific Heuristic Generation and Selection** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.00490)

39. **Learn to Relax with Large Language Models: Solving Nonlinear Combinatorial Optimization Problems via Bidirectional Coevolution** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.12643)

40. **Large Language Models powered Neural Solvers for Generalized Vehicle Routing Problems** ICLR 2025 Workshop AgenticAI, 2025. [paper](https://openreview.net/pdf?id=EVqlVjvlt8), [code](https://github.com/Fsoft-AIC/NCO-LLM)

41. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://neurips.cc/virtual/2025/loc/san-diego/poster/115835), [code](https://github.com/Summer142857/LLMCoSolver)
    *Xia Jiang, Yaoxin Wu, Minshuo Li, Zhiguang Cao, Yingqian Zhang*

42. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://arxiv.org/pdf/2509.16865), [code](https://github.com/Summer142857/LLMCoSolver)

43. **Hierarchical Representations for Cross-task Automated Heuristic Design using LLMs** Under Review, 2025. [paper](https://openreview.net/pdf?id=dgvx86qybJ)

44. **HeurAgenix: Leveraging LLMs for Solving Complex Combinatorial Optimization Challenges** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.15196), [code](https://github.com/microsoft/HeurAgenix)

45. **Glia: A Human-Inspired AI for Automated Systems Design and Optimization** Arxiv, 2025. [paper](https://arxiv.org/abs/2510.27176)

46. **Fitness Landscape of Large Language Model-Assisted Automated Algorithm Search** Arxiv, 2025. [paper](https://arxiv.org/pdf/2504.19636)

47. **Fine-tuning Large Language Model for Automated Algorithm Design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2507.10614)

48. **Efficient Heuristics Generation for Solving Combinatorial Optimization Problems Using Large Language Models** KDD, 2025. [paper](https://arxiv.org/pdf/2505.12627v1), [code](https://github.com/wuuu110/Hercules)

49. **CogMCTS: A Novel Cognitive-Guided Monte Carlo Tree Search Framework for Iterative Heuristic Evolution with Large Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.08609)

50. **COExpander: Adaptive Solution Expansion for Combinatorial Optimization** ICML, 2025. [paper](https://openreview.net/forum?id=KMaBXMWsBM), [code](https://github.com/Thinklab-SJTU/COExpander)
    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

51. **Boosting Neural Combinatorial Optimization for Large-Scale Vehicle Routing Problems** ICLR, 2025. [paper](https://openreview.net/forum?id=TbTJJNjumY)
    *Fu Luo, Xi Lin, Yaoxin Wu, Zhenkun Wang, Tong Xialiang, Mingxuan Yuan, Qingfu Zhang*

52. **AutoEP: LLMs-Driven Automation of Hyperparameter Evolution for Metaheuristic Algorithms** ICLR, 2025. [paper](https://arxiv.org/pdf/2509.23189)

53. **ARS: Automatic Routing Solver with Large Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2502.15359), [code](https://github.com/Ahalikai/ARS-Routbench)

54. **An Agentic Framework with LLMs for Solving Complex Vehicle Routing Problems** Arxiv, 2025. [paper](https://arxiv.org/pdf/2510.16701)

55. **Aligning LLMs with Graph Neural Solvers for Combinatorial Optimization** Under Review, 2025. [paper](https://openreview.net/pdf?id=KSfLDk3jxI)

56. **ACCORD: Autoregressive Constraint-satisfying Generation for COmbinatorial Optimization with Routing and Dynamic attention** Under Review, 2025. [paper](https://openreview.net/pdf?id=f0TBAdcJ8m)

57. **A Mixed-Curvature based Pre-training Paradigm for Multi-Task Vehicle Routing Solver** ICML, 2025. [paper](https://openreview.net/pdf?id=JsPyLqCgks), [code](https://github.com/lsyysl9711/Mixed_Curvature_VRPs)

58. **A Comprehensive Evaluation of Contemporary ML-Based Solvers for Combinatorial Optimization** ICML 2025 Workshop AI4Math, 2025. [paper](https://arxiv.org/pdf/2505.16952), [code](https://huggingface.co/datasets/CO-Bench/FrontierCO)

59. **UNCO: Towards Unifying Neural Combinatorial Optimization through Large Language Model** Arxiv, 2024. [paper](https://arxiv.org/pdf/2408.12214)

60. **UDC: A Unified Neural Divide-and-Conquer Framework for Large-Scale Combinatorial Optimization Problems** NeurIPS, 2024. [paper](https://openreview.net/pdf?id=dCgbyvmlwL), [code](https://github.com/CIAM-Group/NCO_code/tree/main/single_objective/UDC-Large-scale-CO-master)
    *Zhi Zheng, Changliang Zhou, Tong Xialiang, Mingxuan Yuan, Zhenkun Wang*

61. **Toward Learning Generalized Cross-Problem Solving Strategies for Combinatorial Optimization** Under Review, 2024. [paper](https://openreview.net/forum?id=VnaJNW80pN)

62. **Solving Diverse Combinatorial Optimization Problems with a Unified Model** Under Review, 2024. [paper](https://openreview.net/forum?id=Kc3yoIL5oR)

63. **SHIELD: Multi-task Multi-distribution Vehicle Routing Solver with Sparsity & Hierarchy in Efficiently Layered Decoder** ICML, 2024. [paper](https://openreview.net/forum?id=AMbIvaD4Rr)

64. **Self-Guiding Exploration for Combinatorial Problems** NeurIPS, 2024. [paper](https://arxiv.org/pdf/2405.17950), [code](https://github.com/Zangir/LLM-for-CP)

65. **RouteFinder: Towards Foundation Models for Vehicle Routing Problems** TMLR, 2024. [paper](https://arxiv.org/pdf/2406.15007), [code](https://github.com/ai4co/routefinder)

66. **RouteExplainer: An Explanation Framework for Vehicle Routing Problem** PAKDD, 2024. [paper](https://arxiv.org/pdf/2403.03585.pdf), [code](https://github.com/ntt-dkiku/route-explainer)

67. **ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution** NeurIPS, 2024. [paper](https://arxiv.org/pdf/2402.01145), [code](https://github.com/ai4co/reevo)

68. **Neural Combinatorial Optimization for Robust Routing Problem with Uncertain Travel Times** NeurIPS, 2024. [paper](https://openreview.net/pdf?id=DoewNm2uT3)
    *Pei Xiao, Zizhen Zhang, Jinbiao Chen, Jiahai Wang, Zhenzhen Zhang*

69. **MVMoE: Multi-Task Vehicle Routing Solver with Mixture-of-Experts** ICML, 2024. [paper](https://arxiv.org/pdf/2405.01029), [code](https://github.com/RoyalSkye/Routing-MVMoE)

70. **Multi-Task Learning for Routing Problem with Cross-Problem Zero-Shot Generalization** KDD, 2024. [paper](https://arxiv.org/pdf/2402.16891), [code](https://github.com/FeiLiu36/MTNCO)

71. **How Multimodal Integration Boost the Performance of LLM for Optimization: Case Study on Capacitated Vehicle Routing Problems** Arxiv, 2024. [paper](https://arxiv.org/pdf/2403.01757)

72. **GOAL: A Generalist Combinatorial Optimization Agent Learner** ICLR, 2024. [paper](https://arxiv.org/pdf/2406.15079), [code](https://github.com/naver/goal-co)

73. **GLOP: Learning Global Partition and Local Construction for Solving Large-Scale Routing Problems in Real-Time** AAAI, 2024. [paper](https://arxiv.org/abs/2312.08224), [code](https://github.com/henry-yeh/GLOP)
    *Haoran Ye, Jiarui Wang, Helan Liang, Zhiguang Cao, Yong Li, Fanzhang Li*

74. **DRoC: Elevating Large Language Models for Complex Vehicle Routing via Decomposed Retrieval of Constraints** ICLR, 2024. [paper](https://openreview.net/forum?id=s9zoyICZ4k)

75. **Distilling Autoregressive Models to Obtain High-Performance Non-autoregressive Solvers for Vehicle Routing Problems with Faster Inference Speed** AAAI, 2024. [paper](https://arxiv.org/abs/2312.12469), [code](https://github.com/xybFight/GNARKD)
    *Yubin Xiao, Di Wang, Boyang Li, Mingzhao Wang, Xuan Wu, Changliang Zhou, You Zhou*

76. **Collaboration! Towards Robust Neural Methods for Routing Problems** NeurIPS, 2024. [paper](https://openreview.net/forum?id=YfQA78gEFA), [code](https://github.com/RoyalSkye/Routing-CNF)
    *Jianan Zhou, Yaoxin Wu, Zhiguang Cao, Wen Song, Jie Zhang, Zhiqi Shen*

77. **Can Large Language Models Solve Robot Routing?** Arxiv, 2024. [paper](https://arxiv.org/pdf/2403.10795), [code](https://github.com/Zhehui-Huang/LLM_Routing)

78. **CaDA: Cross-Problem Routing Solver with Constraint-Aware Dual-Attention** ICML, 2024. [paper](https://arxiv.org/pdf/2412.00346)

79. **A Scalable Learning Approach for the Capacitated Vehicle Routing Problem** Computers and Operations Research, 2024. [paper](https://dx.doi.org/10.1016/j.cor.2024.106787)
    *James Fitzpatrick, Deepak Ajwani, Paula Carroll*

80. **A Neural Column Generation Approach to the Vehicle Routing Problem with Two-Dimensional Loading and Last-In-First-Out Constraints** IJCAI, 2024. [paper](https://www.ijcai.org/proceedings/2024/0218.pdf), [code](https://github.com/xyfffff/NCG-for-2L-CVRP)
    *Yifan Xia, Xiangyi Zhang*

81. **Winner Takes It All: Training Performant RL Populations for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=v6VpqGcGAR)
    *Nathan Grinsztajn, Daniel Furelos-Blanco, Shikha Surana, Cl{\'e}ment Bonnet, Thomas D Barrett*

82. **Towards Omni-generalizable Neural Methods for Vehicle Routing Problems** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25267), [code](https://github.com/RoyalSkye/Omni-VRP)
    *Zhou Jianan, Yaoxin Wu, Wen Song, Zhiguang Cao, Jie Zhang*

83. **Neural Multi-Objective Combinatorial Optimization with Diversity Enhancement** NeurIPS, 2023. [paper](https://openreview.net/forum?id=N4JkStI1fe), [code](https://github.com/bill-cjb/NHDE)
    *Jinbiao Chen, Zizhen Zhang, Zhiguang Cao, Yaoxin Wu, Yining Ma, Te Ye, Jiahai Wang*

84. **Neural Combinatorial Optimization with Heavy Decoder: Toward Large Scale Generalization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=RBI4oAbdpm), [code](https://github.com/CIAM-Group/NCO_code/tree/main/single_objective/LEHD)
    *Fu Luo, Xi Lin, Fei Liu, Qingfu Zhang, Zhenkun Wang*

85. **Meta-SAGE: Scale Meta-Learning Scheduled Adaptation with Guided Exploration for Mitigating Scale Shift on Combinatorial Optimization** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25138)
    *Jiwoo Son, Minsu Kim, Hyeonah Kim, Jinkyoo Park*

86. **Learning to Search Feasible and Infeasible Regions of Routing Problems with Flexible Neural k-Opt** NeurIPS, 2023. [paper](https://openreview.net/forum?id=q1JukwH2yP), [code](https://github.com/yining043/NeuOpt)
    *Yining Ma, Zhiguang Cao, Yeow Meng Chee*

87. **Learning to Prune Electric Vehicle Routing Problems** LION, 2023. [paper](https://link.springer.com/chapter/10.1007/978-3-031-44505-7_26)
    *James Fitzpatrick, Deepak Ajwani, Paula Carroll*

88. **Learning to CROSS exchange to solve min-max vehicle routing problems** ICLR, 2023. [paper](https://openreview.net/forum?id=ZcnzsHC10Y)
    *Minjun Kim, Junyoung Park, Jinkyoo Park*

89. **Generalize Learned Heuristics to Solve Large-scale Vehicle Routing Problems in Real-time** ICLR, 2023. [paper](https://openreview.net/forum?id=6ZajpxqTlQ)
    *Qingchun Hou, Jingwei Yang, Yiqiang Su, Xiaoqing Wang, Yuming Deng*

90. **Ensemble-based Deep Reinforcement Learning for Vehicle Routing Problems under Distribution Shift** NeurIPS, 2023. [paper](https://openreview.net/forum?id=HoBbZ1vPAh)
    *Yuan Jiang, Zhiguang Cao, Yaoxin Wu, Wen Song, Jie Zhang*

91. **Efficient Training of Multi-task Combinatorial Neural Solver with Multi-armed Bandits** TMLR, 2023. [paper](https://arxiv.org/pdf/2305.06361)

92. **Efficient Meta Neural Heuristic for Multi-Objective Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=593fc38lhN), [code](https://github.com/bill-cjb/EMNH)
    *Jinbiao Chen, Jiahai Wang, Zizhen Zhang, Zhiguang Cao, Te Ye, Siyuan Chen*

93. **DeepACO: Neural-enhanced Ant Systems for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=cd5D1DD923), [code](https://github.com/henry-yeh/DeepACO)
    *Haoran Ye, Jiarui Wang, Zhiguang Cao, Helan Liang, Yong Li*

94. **Combinatorial Optimization with Policy Adaptation using Latent Space Search** NeurIPS, 2023. [paper](https://openreview.net/forum?id=vpMBqdt9Hl)
    *Felix Chalumeau, Shikha Surana, Cl{\'e}ment Bonnet, Nathan Grinsztajn, Arnu Pretorius, Alexandre Laterre, Thomas D Barrett*

95. **BQ-NCO: Bisimulation Quotienting for Efficient Neural Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=BRqlkTDvvm), [code](https://github.com/naver/bq-nco)
    *Darko Drakulic, Sofia Michel, Florian Mai, Arnaud Sors, Jean-Marc Andreoli*

96. **Sym-NCO: Leveraging Symmetricity for Neural Combinatorial Optimization** NeurIPS, 2022. [paper](https://openreview.net/forum?id=kHrE2vi5Rvs), [code](https://github.com/alstn12088/Sym-NCO)
    *Minsu Kim, Junyoung Park, Jinkyoo Park*

97. **Simulation-guided Beam Search for Neural Combinatorial Optimization** NeurIPS, 2022. [paper](https://openreview.net/forum?id=tYAS1Rpys5), [code](https://github.com/yd-kwon/SGBS)
    *Jinho Choo, Yeong-Dae Kwon, Jihoon Kim, Jeongwoo Jae, Andr{\'e} Hottung, Kevin Tierney, Youngjune Gwon*

98. **Preference Conditioned Neural Multi-objective Combinatorial Optimization** ICLR, 2022. [paper](https://openreview.net/forum?id=QuObT9BTWo)
    *Xi Lin, Zhiyuan Yang, Qingfu Zhang*

99. **Learning Generalizable Models for Vehicle Routing Problems via Knowledge Distillation** NeurIPS, 2022. [paper](https://openreview.net/forum?id=sOVNpUEgKMp), [code](https://github.com/jieyibi/AMDKD)
    *Jieyi Bi, Yining Ma, Jiahai Wang, Zhiguang Cao, Jinbiao Chen, Yuan Sun, Yeow Meng Chee*

100. **RP-DQN: An application of Q-Learning to Vehicle Routing Problems** Arxiv, 2021. [paper](https://arxiv.org/abs/2104.12226)
    *Ahmad Bdeir, Simon Boeder, Tim Dernedde, Kirill Tkachuk, Jonas K Falkner, Lars Schmidt-Thieme*

101. **Reinforcement Learning for Route Optimization with Robustness Guarantees** IJCAI, 2021. [paper](https://www.ijcai.org/proceedings/2021/0357.pdf)
    *Tobias Jacobs, Francesco Alesiani, Gulcin Ermis*

102. **Multi-Decoder Attention Model with Embedding Glimpse for Solving Vehicle Routing Problems.** AAAI, 2021. [paper](https://arxiv.org/abs/2012.10638), [code](https://github.com/liangxinedu/MDAM)
    *Liang Xin, Wen Song, Zhiguang Cao, Jie Zhang*

103. **Learning to Delegate for Large-scale Vehicle Routing** NeurIPS, 2021. [paper](https://proceedings.neurips.cc/paper/2021/hash/dc9fa5f217a1e57b8a6adeb065560b38-Abstract.html)
    *Sirui Li, Zhongxia Yan, Cathy Wu*

104. **Learning Improvement Heuristics for Solving Routing Problems** TNNLS, 2021. [paper](https://ieeexplore.ieee.org/abstract/document/9393606?casa_token=mFeyLmrOGfIAAAAA:nmAkjUaTSooYurWHuWGYNoguV453anw9Enyv45xG5jb2oCps6QE4A1CFe1EmFmTzbON6cL5maw)
    *Yaoxin Wu, Wen Song, Zhiguang Cao, Jie Zhang, Andrew Lim*

105. **Learning a Latent Search Space for Routing Problems using Variational Autoencoders** ICLR, 2021. [paper](https://openreview.net/forum?id=90JprVrJBO)
    *Andre Hottung, Bhanu Bhandari, Kevin Tierney*

106. **Deep Policy Dynamic Programming for Vehicle Routing Problems** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.11756)
    *Wouter Kool, Herke van Hoof, Joaquim Gromicho, Max Welling*

107. **Analytics and Machine Learning in Vehicle Routing Research** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.10012)
    *Ruibin Bai, Xinan Chen, Zhi-Long Chen, Tianxiang Cui, Shuhui Gong, Wentao He, Xiaoping Jiang, Huan Jin, Jiahuan Jin, Graham Kendall, others*

108. **Reinforcement Learning with Combinatorial Actions: An Application to Vehicle Routing** NeurIPS, 2020. [paper](https://papers.nips.cc/paper/2020/file/06a9d51e04213572ef0720dd27a84792-Paper.pdf), [code](https://github.com/google-research/tf-opt)
    *Arthur Delarue, Ross Anderson, Christian Tjandraatmadja*

109. **Neural Large Neighborhood Search for the Capacitated Vehicle Routing Problem** Arxiv, 2020. [paper](https://arxiv.org/abs/1911.09539)
    *Andre Hottung, Kevin Tierney*

110. **Efficiently Solving the Practical,Vehicle Routing Problem: A Novel Joint Learning Approach.** KDD, 2020. [paper](https://www.kdd.org/kdd2020/accepted-papers/view/efficiently-solving-the-practical-vehicle-routing-problem-a-novel-joint-lea)
    *Lu Duan, Yang Zhan, Haoyuan Hu, Yu Gong, Jiangwen Wei, Xiaodong Zhang, Yinghui Xu*

111. **Deep Reinforcement Learning for the Electric Vehicle Routing Problem with Time Windows.** Arxiv, 2020. [paper](https://arxiv.org/abs/2010.02068)
    *Bo Lin, Bissan Ghaddar, Jatin Nathwani*

112. **A Learning-based Iterative Method for Solving Vehicle Routing Problems** ICLR, 2020. [paper](https://static.aminer.cn/upload/pdf/program/5e5e18dd93d709897ce3720b_0.pdf)
    *Hao Lu, Xingwen Zhang, Shuang Yang*

113. **Learning to Perform Local Rewriting for Combinatorial Optimization.** NeurIPS, 2019. [paper](https://arxiv.org/abs/1810.00337), [code](https://github.com/facebookresearch/neural-rewriter)
    *Xinyun Chen, Yuandong Tian*

### [Maximum Independent Set](#content) · *42 papers*

1. **Native Adaptive Solution Expansion for Diffusion-based Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=084SvT55yk)
    *Yu Wang, Yang Li, Jiale Ma, Junchi Yan, Yi Chang*

2. **MaskCO: Masked Generation Drives Effective Representation Learning and Exploiting for Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=psUjNnLhl9), [code](https://github.com/Thinklab-SJTU/MaskCO)
    *Lvda Chen, Yang Li, Junchi Yan*

3. **Hard Constraints Meet Soft Generation: Guaranteed Feasibility for LLM-based Combinatorial Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.01090)

4. **FrontierCO: Real-World and Large-Scale Evaluation of Machine Learning Solvers for Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=BVprkacwFY), [code](https://github.com/sunnweiwei/FrontierCO)
    *Shengyu Feng, Weiwei Sun, Shanda Li, Ameet Talwalkar, Yiming Yang*

5. **ConRep4CO: Contrastive Representation Learning of Combinatorial Optimization Instances across Types** ICLR, 2026. [paper](https://openreview.net/forum?id=OXRnvOOiAf), [code](https://github.com/Thinklab-SJTU/ConRep4CO)
    *Ziao Guo, Yang Li, Shiyue Wang, Junchi Yan*

6. **Scalable Discrete Diffusion Samplers: Combinatorial Optimization and Statistical Physics** ICLR, 2025. [paper](https://openreview.net/pdf?id=peNgxpbdxB)
    *Sebastian Sanokowski, Wilhelm Franz Berghammer, Haoyu Peter Wang, Martin Ennemoser, Sepp Hochreiter, Sebastian Lehner*

7. **OPT-BENCH: Evaluating LLM Agent on Large-Scale Search Spaces Optimization Problems** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.10764), [code](https://github.com/OliverLeeXZ/OPT-BENCH)

8. **ML4CO-Bench-101: Benchmark Machine Learning for Classic Combinatorial Problems on Graphs** NeurIPS, 2025. [paper](https://openreview.net/forum?id=ye4ntB1Kzi), [code](https://github.com/Thinklab-SJTU/ML4CO-Bench-101)
    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

9. **Learning to Explore and Exploit with GNNs for Unsupervised Combinatorial Optimization** ICLR, 2025. [paper](https://openreview.net/forum?id=vaJ4FObpXN), [code](https://github.com/utkuumur/X2GNN)
    *Utku Umur Acikalin, Aaron M. Ferber, Carla P. Gomes*

10. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://neurips.cc/virtual/2025/loc/san-diego/poster/115835), [code](https://github.com/Summer142857/LLMCoSolver)
    *Xia Jiang, Yaoxin Wu, Minshuo Li, Zhiguang Cao, Yingqian Zhang*

11. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://arxiv.org/pdf/2509.16865), [code](https://github.com/Summer142857/LLMCoSolver)

12. **Improving Existing Optimization Algorithms with LLMs** Arxiv, 2025. [paper](https://arxiv.org/pdf/2502.08298)

13. **GraphThought: Graph Combinatorial Optimization with Thought Generation** Arxiv, 2025. [paper](https://arxiv.org/pdf/2502.11607)

14. **GraphArena: Evaluating and Exploring Large Language Models on Graph Computation** ICLR, 2025. [paper](https://openreview.net/pdf?id=Y1r9yCMzeA), [code](https://github.com/squareRoot3/GraphArena/tree/master)

15. **COExpander: Adaptive Solution Expansion for Combinatorial Optimization** ICML, 2025. [paper](https://openreview.net/forum?id=KMaBXMWsBM), [code](https://github.com/Thinklab-SJTU/COExpander)
    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

16. **Aligning LLMs with Graph Neural Solvers for Combinatorial Optimization** Under Review, 2025. [paper](https://openreview.net/pdf?id=KSfLDk3jxI)

17. **A Comprehensive Evaluation of Contemporary ML-Based Solvers for Combinatorial Optimization** ICML 2025 Workshop AI4Math, 2025. [paper](https://arxiv.org/pdf/2505.16952), [code](https://huggingface.co/datasets/CO-Bench/FrontierCO)

18. **Solving Diverse Combinatorial Optimization Problems with a Unified Model** Under Review, 2024. [paper](https://openreview.net/forum?id=Kc3yoIL5oR)

19. **MARCO: A Memory-Augmented Reinforcement Framework for Combinatorial Optimization** IJCAI, 2024. [paper](https://www.ijcai.org/proceedings/2024/0766.pdf), [code](https://github.com/TheLeprechaun25/MARCO)
    *Andoni I. Garmendia, Quentin Cappart, Josu Ceberio, Alexander Mendiburu*

20. **GOAL: A Generalist Combinatorial Optimization Agent Learner** ICLR, 2024. [paper](https://arxiv.org/pdf/2406.15079), [code](https://github.com/naver/goal-co)

21. **Fast T2T: Optimization Consistency Speeds Up Diffusion-Based Training-to-Testing Solving for Combinatorial Optimization** NeurIPS, 2024. [paper](https://openreview.net/pdf?id=xDrKZOZEOc), [code](https://github.com/Thinklab-SJTU/Fast-T2T)
    *Yang Li, Jinpei Guo, Runzhong Wang, Hongyuan Zha, Junchi Yan*

22. **Efficient Combinatorial Optimization via Heat Diffusion** NeurIPS, 2024. [paper](https://openreview.net/forum?id=psDrko9v1D), [code](https://github.com/AwakerMhy/HeO)
    *Hengyuan Ma, Wenlian Lu, Jianfeng Feng*

23. **Distributed Constrained Combinatorial Optimization leveraging Hypergraph Neural Networks** Nature Machine Intelligence, 2024. [paper](https://arxiv.org/abs/2311.09375), [code](https://github.com/nasheydari/HypOp)
    *Nasimeh Heydaribeni, Xinrui Zhan, Ruisi Zhang, Tina Eliassi-Rad, Farinaz Koushanfar*

24. **Controlling Continuous Relaxation for Combinatorial Optimization** NeurlPS, 2024. [paper](https://openreview.net/pdf?id=ykACV1IhjD)
    *Yuma Ichikawa*

25. **A Diffusion Model Framework for Unsupervised Neural Combinatorial Optimization** ICML, 2024. [paper](https://arxiv.org/abs/2406.01661), [code](https://github.com/ml-jku/DIffUCO)
    *Sebastian Sanokowski, Sepp Hochreiter, Sebastian Lehner*

26. **Variational Annealing on Graphs for Combinatorial Optimization** NeurlPS, 2023. [paper](https://openreview.net/forum?id=SLx7paoaTU), [code](https://github.com/ml-jku/VAG-CO)
    *Sebastian Sanokowski, Wilhelm Franz Berghammer, Sepp Hochreiter, Sebastian Lehner*

27. **Unsupervised Learning for Combinatorial Optimization Needs Meta Learning** ICLR, 2023. [paper](https://openreview.net/forum?id=-ENYHCE8zBp), [code](https://github.com/Graph-COM/Meta_CO)
    *Haoyu Wang, Pan Li*

28. **T2T: From Distribution Learning in Training to Gradient Search in Testing for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=JtF0ugNMv2), [code](https://github.com/Thinklab-SJTU/T2TCO)
    *Yang Li, Jinpei Guo, Runzhong Wang, Junchi Yan*

29. **ROCO: A General Framework for Evaluating Robustness of Combinatorial Optimization Solvers on Graphs** ICLR, 2023. [paper](https://openreview.net/forum?id=2r6YMqz4Mml), [code](https://github.com/Thinklab-SJTU/ROCO)
    *Han Lu, Zenan Li, Runzhong Wang, Qibing Ren, Xijun Li, Mingxuan Yuan, Jia Zeng, Xiaokang Yang, Junchi Yan*

30. **Revisiting Sampling for Combinatorial Optimization** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/23661)
    *Haoran, Goshvadi Katayoon, Nova Azade, Schuurmans Dale Sun, Dai Hanjun.*

31. **Maximum Independent Set: Self-Training through Dynamic Programming** NeurlPS, 2023. [paper](https://openreview.net/forum?id=igE3Zbxvws), [code](https://github.com/LIONS-EPFL/dynamic-MIS)
    *Lorenzo Brusca, Lars CPM Quaedvlieg, Stratis Skoulakis, Grigorios G Chrysos, Volkan Cevher*

32. **Let the Flows Tell: Solving Graph Combinatorial Optimization Problems with GFlowNets** NeurlPS, 2023. [paper](https://arxiv.org/abs/2305.17010), [code](https://github.com/zdhNarsil/GFlowNet-CombOpt)
    *Dinghuai Zhang, Hanjun Dai, Nikolay Malkin, Aaron Courville, Yoshua Bengio, Ling Pan*

33. **Graph-based Deterministic Policy Gradient for Repetitive Combinatorial Optimization Problems** ICLR, 2023. [paper](https://openreview.net/forum?id=yHIIM9BgOo), [code](https://github.com/XzrTGMu/twin-nphard)
    *Zhongyuan Zhao, Ananthram Swami, Santiago Segarra*

34. **DISCS: A Benchmark for Discrete Sampling** NeurlPS, 2023. [paper](https://openreview.net/forum?id=oi1MUMk5NF), [code](https://github.com/google-research/discs)
    *Katayoon Goshvadi, Haoran Sun, Xingchao Liu, Azade Nova, Ruqi Zhang, Will Sussman Grathwohl, Dale Schuurmans, Hanjun Dai*

35. **DIFUSCO: Graph-based Diffusion Solvers for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=JV8Ff0lgVV), [code](https://github.com/Edward-Sun/DIFUSCO)
    *Zhiqing Sun, Yiming Yang*

36. **What's Wrong with Deep Learning in Tree Search for Combinatorial Optimization** ICLR, 2022. [paper](https://openreview.net/forum?id=mk0HzdqY7i1), [code](https://github.com/MaxiBoether/mis-benchmark-framework)
    *Maximilian Bother, Otto Kissig, Martin Taraz, Sarel Cohen, Karen Seidel, Tobias Friedrich*

37. **Optimistic tree search strategies for black-box combinatorial optimization** NeurlPS, 2022. [paper](https://openreview.net/forum?id=JGLW4DvX11F)
    *Cedric Malherbe, Antoine Grosnit, Rasul Tutunov, Haitham Bou Ammar, Jun Wang*

38. **Solving Graph-based Public Good Games with Tree Search and Imitation Learning** NeurlPS, 2021. [paper](https://arxiv.org/abs/2106.06762)
    *Victor-Alexandru Darvariu, Stephen Hailes, Mirco Musolesi*

39. **NN-Baker: A Neural-network Infused Algorithmic Framework for Optimization Problems on Geometric Intersection Graphs** NeurlPS, 2021. [paper](https://papers.nips.cc/paper/2021/file/c236337b043acf93c7df397fdb9082b3-Paper.pdf)
    *Evan McCarty, Qi Zhao, Anastasios Sidiropoulos, Yusu Wang*

40. **Distributed Scheduling Using Graph Neural Networks** ICASSP, 2021. [paper](https://ieeexplore.ieee.org/abstract/document/9414098?casa_token=Q4coRBbINPMAAAAA:0T8L49Kyn9p4CoM20-FqINKCyk_Sm3ye5TemPT8GlG3C3wXXLvn1RGKeHgriiyZIcg_GFB4z1A)
    *Zhongyuan Zhao, Gunjan Verma, Chirag Rao, Ananthram Swami, Santiago Segarra*

41. **Learning What to Defer for Maximum Independent Sets** ICML, 2020. [paper](http://proceedings.mlr.press/v119/ahn20a.html)
    *Sungsoo Ahn, Younggyo Seo, Jinwoo Shin*

42. **Combinatorial Optimization with Graph Convolutional Networks and Guided Tree Search.** NeurIPS, 2018. [paper](https://arxiv.org/abs/1810.10659)
    *Zhuwen Li, Qifeng Chen, Vladlen Koltun*

### [Generalization](#content) · *13 papers*

1. **EvoX: Meta-Evolution for Automated Discovery** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.23413), [code](https://github.com/skydiscover-ai/skydiscover)

2. **Evolving Interdependent Operators with Large Language Models for Multi-Objective Combinatorial Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.17899)

3. **AVO: Agentic Variation Operators for Autonomous Evolutionary Search** Arxiv, 2026. [paper](https://arxiv.org/pdf/2603.24517)

4. **AdaEvolve: Adaptive LLM Driven Zeroth-Order Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.20133), [code](https://github.com/skydiscover-ai/skydiscover)

5. **ThetaEvolve: Test-time Learning on Open Problems** Arxiv, 2025. [paper](https://arxiv.org/abs/2511.23473)

6. **LLM-based Instance-driven Heuristic Bias in the Context of a Biased Random Key Genetic Algorithm** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.09707)

7. **GOAL: A Generalist Combinatorial Optimization Agent Learner** ICLR, 2025. [paper](https://openreview.net/forum?id=z2z9suDRjw)
    *Darko Drakulic, Sofia Michel, Jean-Marc Andreoli*

8. **Towards Omni-generalizable Neural Methods for Vehicle Routing Problems** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25267), [code](https://github.com/RoyalSkye/Omni-VRP)
    *Zhou Jianan, Yaoxin Wu, Wen Song, Zhiguang Cao, Jie Zhang*

9. **ROCO: A General Framework for Evaluating Robustness of Combinatorial Optimization Solvers on Graphs** ICLR, 2023. [paper](https://openreview.net/forum?id=2r6YMqz4Mml), [code](https://github.com/Thinklab-SJTU/ROCO)
    *Han Lu, Zenan Li, Runzhong Wang, Qibing Ren, Xijun Li, Mingxuan Yuan, Jia Zeng, Xiaokang Yang, Junchi Yan*

10. **Learning for Robust Combinatorial Optimization: Algorithm and Application** INFOCOM, 2022. [paper](https://ieeexplore.ieee.org/abstract/document/9796715/)
    *Zhihui Shao, Jianyi Yang, Cong Shen, Shaolei Ren*

11. **Generalization of Neural Combinatorial Solvers Through the Lens of Adversarial Robustness** ICLR, 2022. [paper](https://openreview.net/forum?id=vJZ7dPIjip3)
    *Simon Geisler, Johanna Sommer, Jan Schuchardt, Aleksandar Bojchevski, Stephan Günnemann*

12. **Learning TSP Requires Rethinking Generalization** CP, 2021. [paper](https://arxiv.org/pdf/2006.07054.pdf), [code](https://github.com/chaitjo/learning-tsp)
    *Chaitanya K. Joshi, Quentin Cappart, Louis-Martin Rousseau, Thomas Laurent*

13. **It's Not What Machines Can Learn It's What We Cannot Teach** ICML, 2020. [paper](http://proceedings.mlr.press/v119/yehuda20a/yehuda20a.pdf)
    *Gal Yehuda, Moshe Gabel, Assaf Schuster*

### [Orienteering Problem](#content) · *24 papers*

1. **PathWise: Planning through World Model for Automated Heuristic Design via Self-Evolving LLMs** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.20539)

2. **Hard Constraints Meet Soft Generation: Guaranteed Feasibility for LLM-based Combinatorial Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.01090)

3. **RoCo: Role-Based LLMs Collaboration for Automatic Heuristic Design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.03762)

4. **OR-LLM-Agent: Automating Modeling and Solving of Operations Research Optimization Problem with Reasoning Large Language Model** Arxiv, 2025. [paper](https://arxiv.org/pdf/2503.10009), [code](https://github.com/bwz96sco/or_llm_agent)

5. **MOTIF: Multi-strategy Optimization via Turn-based Interactive Framework** AAAI, 2025. [paper](https://arxiv.org/abs/2508.03929), [code](https://github.com/HaiAu2501/MOTIF)

6. **MeLA: A Metacognitive LLM-Driven Architecture for Automatic Heuristic Design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2507.20541), [code](https://github.com/Qzs1335/MeLA)

7. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://arxiv.org/pdf/2509.16865), [code](https://github.com/Summer142857/LLMCoSolver)

8. **LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.14138)

9. **Efficient Heuristics Generation for Solving Combinatorial Optimization Problems Using Large Language Models** KDD, 2025. [paper](https://arxiv.org/pdf/2505.12627v1), [code](https://github.com/wuuu110/Hercules)

10. **EALG: Evolutionary Adversarial Generation of Language Model–Guided Generators for Combinatorial Optimization** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.02594)

11. **CogMCTS: A Novel Cognitive-Guided Monte Carlo Tree Search Framework for Iterative Heuristic Evolution with Large Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.08609)

12. **CALM: Co-evolution of Algorithms and Language Model for Automatic Heuristic Design** ICLR, 2025. [paper](https://arxiv.org/pdf/2505.12285v1)

13. **UDC: A Unified Neural Divide-and-Conquer Framework for Large-Scale Combinatorial Optimization Problems** NeurIPS, 2024. [paper](https://openreview.net/pdf?id=dCgbyvmlwL), [code](https://github.com/CIAM-Group/NCO_code/tree/main/single_objective/UDC-Large-scale-CO-master)
    *Zhi Zheng, Changliang Zhou, Tong Xialiang, Mingxuan Yuan, Zhenkun Wang*

14. **Toward Learning Generalized Cross-Problem Solving Strategies for Combinatorial Optimization** Under Review, 2024. [paper](https://openreview.net/forum?id=VnaJNW80pN)

15. **Solving Diverse Combinatorial Optimization Problems with a Unified Model** Under Review, 2024. [paper](https://openreview.net/forum?id=Kc3yoIL5oR)

16. **Self-Guiding Exploration for Combinatorial Problems** NeurIPS, 2024. [paper](https://arxiv.org/pdf/2405.17950), [code](https://github.com/Zangir/LLM-for-CP)

17. **ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution** NeurIPS, 2024. [paper](https://arxiv.org/pdf/2402.01145), [code](https://github.com/ai4co/reevo)

18. **HSEvo: Elevating Automatic Heuristic Design with Diversity-Driven Harmony Search and Genetic Algorithm Using LLMs** AAAI, 2024. [paper](https://arxiv.org/pdf/2412.14995), [code](https://github.com/datphamvn/HSEvo)

19. **GOAL: A Generalist Combinatorial Optimization Agent Learner** ICLR, 2024. [paper](https://arxiv.org/pdf/2406.15079), [code](https://github.com/naver/goal-co)

20. **Cross-Problem Learning for Solving Vehicle Routing Problems** IJCAI, 2024. [paper](https://arxiv.org/pdf/2404.11677), [code](https://github.com/Zhuoyi-Lin/Cross_problem_learning)

21. **Meta-SAGE: Scale Meta-Learning Scheduled Adaptation with Guided Exploration for Mitigating Scale Shift on Combinatorial Optimization** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25138)
    *Jiwoo Son, Minsu Kim, Hyeonah Kim, Jinkyoo Park*

22. **Efficient Training of Multi-task Combinatorial Neural Solver with Multi-armed Bandits** TMLR, 2023. [paper](https://arxiv.org/pdf/2305.06361)

23. **DeepACO: Neural-enhanced Ant Systems for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=cd5D1DD923), [code](https://github.com/henry-yeh/DeepACO)
    *Haoran Ye, Jiarui Wang, Zhiguang Cao, Helan Liang, Yong Li*

24. **A reinforcement learning approach to the orienteering problem with time windows** Computers & Operations Research, 2021. [paper](https://arxiv.org/abs/2011.03647v2), [code](https://github.com/mustelideos/optw_rl)
    *Ricardo Gama, Hugo L. Fernandes*

### [Knapsack](#content) · *41 papers*

1. **Rethinking LLM-Driven Heuristic Design: Generating Efficient and Specialized Solvers via Dynamics-Aware Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.20868)

2. **PathWise: Planning through World Model for Automated Heuristic Design via Self-Evolving LLMs** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.20539)

3. **DRAGON: LLM-Driven Decomposition and Reconstruction Agents for Large-Scale Combinatorial Optimization** AAMAS, 2026. [paper](https://arxiv.org/abs/2601.06502)
    *Shengkai Chen, Zhiguang Cao, Jianan Zhou, Yaoxin Wu, Senthilnath Jayavelu, Zhuoyi Lin, Xiaoli Li, Shili Xiang*

4. **Beyond the Node: Clade-level Selection for Efficient MCTS in Automatic Heuristic Design** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.00549)

5. **TPD-AHD: Textual Preference Differentiation for LLM-Based Automatic Heuristic Design** Under Review, 2025. [paper](https://openreview.net/pdf?id=VEMknlIPtM)

6. **RoCo: Role-Based LLMs Collaboration for Automatic Heuristic Design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.03762)

7. **Rethinking Neural Multi-Objective Combinatorial Optimization via Neat Weight Embedding** ICLR, 2025. [paper](https://openreview.net/forum?id=GM7cmQfk2F)
    *Jinbiao Chen, Zhiguang Cao, Jiahai Wang, Yaoxin Wu, Hanzhang Qin, Zizhen Zhang, Yue-Jiao Gong*

8. **RedAHD: Reduction-Based End-to-End Automatic Heuristic Design with Large Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2505.20242)

9. **Pareto-Grid-Guided Large Language Models for Fast and High-Quality Heuristics Design in Multi-Objective Combinatorial Optimization** AAAI, 2025. [paper](https://arxiv.org/pdf/2507.20923), [code](https://github.com/langkhachhoha/MPaGE)

10. **OptiHive: Ensemble Selection for LLM-Based Optimization via Statistical Modeling** Arxiv, 2025. [paper](https://arxiv.org/pdf/2508.02503)

11. **OPT-BENCH: Evaluating LLM Agent on Large-Scale Search Spaces Optimization Problems** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.10764), [code](https://github.com/OliverLeeXZ/OPT-BENCH)

12. **Nested-Refinement Metamorphosis: Reflective Evolution for Efficient Optimization of Networking Problems** ACL, 2025. [paper](https://aclanthology.org/2025.findings-acl.895.pdf)

13. **MOTIF: Multi-strategy Optimization via Turn-based Interactive Framework** AAAI, 2025. [paper](https://arxiv.org/abs/2508.03929), [code](https://github.com/HaiAu2501/MOTIF)

14. **Monte Carlo Tree Search for Comprehensive Exploration in LLM-Based Automatic Heuristic Design** ICML, 2025. [paper](https://arxiv.org/pdf/2501.08603), [code](https://github.com/zz1358m/MCTS-AHD-master)

15. **Know the Ropes: A Heuristic Strategy for LLM-based Multi-Agent System Design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2505.16979)

16. **HeurAgenix: Leveraging LLMs for Solving Complex Combinatorial Optimization Challenges** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.15196), [code](https://github.com/microsoft/HeurAgenix)

17. **Efficient Heuristics Generation for Solving Combinatorial Optimization Problems Using Large Language Models** KDD, 2025. [paper](https://arxiv.org/pdf/2505.12627v1), [code](https://github.com/wuuu110/Hercules)

18. **CogMCTS: A Novel Cognitive-Guided Monte Carlo Tree Search Framework for Iterative Heuristic Evolution with Large Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.08609)

19. **CALM: Co-evolution of Algorithms and Language Model for Automatic Heuristic Design** ICLR, 2025. [paper](https://arxiv.org/pdf/2505.12285v1)

20. **Behavior and Representation in Large Language Models for Combinatorial Optimization: From Feature Extraction to Algorithm Selection** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.13374)

21. **Approximation algorithms for combinatorial optimization with predictions** ICLR, 2025. [paper](https://openreview.net/forum?id=AEFVa6VMu1)
    *Antonios Antoniadis, Marek Elias, Adam Polak, Moritz Venzin*

22. **Aligning LLMs with Graph Neural Solvers for Combinatorial Optimization** Under Review, 2025. [paper](https://openreview.net/pdf?id=KSfLDk3jxI)

23. **Adversarial examples for heuristics in combinatorial optimization: An LLM based approach** Under Review, 2025. [paper](https://openreview.net/pdf?id=fasU6t3hL4)

24. **ACCORD: Autoregressive Constraint-satisfying Generation for COmbinatorial Optimization with Routing and Dynamic attention** Under Review, 2025. [paper](https://openreview.net/pdf?id=f0TBAdcJ8m)

25. **UNCO: Towards Unifying Neural Combinatorial Optimization through Large Language Model** Arxiv, 2024. [paper](https://arxiv.org/pdf/2408.12214)

26. **Towards a Generic Representation of Combinatorial Problems for Learning-Based Approaches** CPAIOR, 2024. [paper](https://arxiv.org/pdf/2403.06026), [code](https://github.com/corail-research/learning-generic-csp)

27. **Solving Diverse Combinatorial Optimization Problems with a Unified Model** Under Review, 2024. [paper](https://openreview.net/forum?id=Kc3yoIL5oR)

28. **Self-Guiding Exploration for Combinatorial Problems** NeurIPS, 2024. [paper](https://arxiv.org/pdf/2405.17950), [code](https://github.com/Zangir/LLM-for-CP)

29. **ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution** NeurIPS, 2024. [paper](https://arxiv.org/pdf/2402.01145), [code](https://github.com/ai4co/reevo)

30. **GOAL: A Generalist Combinatorial Optimization Agent Learner** ICLR, 2024. [paper](https://arxiv.org/pdf/2406.15079), [code](https://github.com/naver/goal-co)

31. **Winner Takes It All: Training Performant RL Populations for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=v6VpqGcGAR)
    *Nathan Grinsztajn, Daniel Furelos-Blanco, Shikha Surana, Cl{\'e}ment Bonnet, Thomas D Barrett*

32. **NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes** ACL, 2023. [paper](https://arxiv.org/pdf/2312.14890), [code](https://github.com/casmlab/NPHardEval)

33. **Neural Multi-Objective Combinatorial Optimization with Diversity Enhancement** NeurIPS, 2023. [paper](https://openreview.net/forum?id=N4JkStI1fe), [code](https://github.com/bill-cjb/NHDE)
    *Jinbiao Chen, Zizhen Zhang, Zhiguang Cao, Yaoxin Wu, Yining Ma, Te Ye, Jiahai Wang*

34. **Efficient Training of Multi-task Combinatorial Neural Solver with Multi-armed Bandits** TMLR, 2023. [paper](https://arxiv.org/pdf/2305.06361)

35. **Efficient Meta Neural Heuristic for Multi-Objective Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=593fc38lhN), [code](https://github.com/bill-cjb/EMNH)
    *Jinbiao Chen, Jiahai Wang, Zizhen Zhang, Zhiguang Cao, Te Ye, Siyuan Chen*

36. **DeepACO: Neural-enhanced Ant Systems for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=cd5D1DD923), [code](https://github.com/henry-yeh/DeepACO)
    *Haoran Ye, Jiarui Wang, Zhiguang Cao, Helan Liang, Yong Li*

37. **BQ-NCO: Bisimulation Quotienting for Efficient Neural Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=BRqlkTDvvm), [code](https://github.com/naver/bq-nco)
    *Darko Drakulic, Sofia Michel, Florian Mai, Arnaud Sors, Jean-Marc Andreoli*

38. **Provably Good Solutions to the Knapsack Problem via Neural Networks of Bounded Size** AAAI, 2021. [paper](https://pubsonline.informs.org/doi/abs/10.1287/ijoc.2021.0225)
    *Christoph Hertrich, Martin Skutella*

39. **A Novel Method to Solve Neural Knapsack Problems** ICML, 2021. [paper](http://proceedings.mlr.press/v139/li21m.html)
    *Duanshun Li, Jing Liu, Dongeun Lee, Ali Seyedmazloom, Giridhar Kaushik, Kookjin Lee, Noseong Park*

40. **An Investigation into Prediction + Optimisation for the Knapsack Problem** CPAIOR, 2019. [paper](https://link.springer.com/chapter/10.1007/978-3-030-19212-9_16)
    *Emir Demirovic, Peter J. Stuckey, James Bailey, Jeffrey Chan, Chris Leckie, Kotagiri Ramamohanarao, Tias Guns*

41. **A Pointer Network Based Deep Learning Algorithm  for 0-1 Knapsack Problem** ICACI, 2018. [paper](https://ieeexplore.ieee.org/abstract/document/8377505)
    *Shenshen Gu, Hao Tao*

### [Boolean Satisfiability](#content) · *49 papers*

1. **HeuriGym: An Agentic Benchmark for LLM-Crafted Heuristics in Combinatorial Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2506.07972), [code](https://github.com/cornell-zhang/heurigym)
    *Hongzheng Chen, Yingheng Wang, Yaohui Cai, Hins Hu, Jiajie Li, Shirley Huang, Chenhui Deng, Rongjian Liang, Shufeng Kong, Haoxing Ren, Samitha Samaranayake, Carla P. Gomes, Zhiru Zhang*

2. **From Heuristic Selection to Automated Algorithm Design: LLMs Benefit from Strong Priors** Arxiv, 2026. [paper](https://arxiv.org/pdf/2603.02792), [code](https://github.com/BaronH07/BAG)

3. **X-evolve: Solution space evolution powered by large language models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2508.07932)

4. **UniCO: On Unified Combinatorial Optimization via Problem Reduction to Matrix-Encoded General TSP** ICLR, 2025. [paper](https://openreview.net/forum?id=yEwakMNIex), [code](https://github.com/Thinklab-SJTU/UniCO)
    *Wenzheng Pan, Hao Xiong, Jiale Ma, Wentao Zhao, Yang Li, Junchi Yan*

5. **Text2Zinc: A Cross-Domain Dataset for Modeling Optimization and Satisfaction Problems in MiniZinc** Arxiv, 2025. [paper](https://arxiv.org/pdf/2503.10642), [code](https://huggingface.co/datasets/skadio/text2zinc)

6. **STRCMP: Integrating Graph Structural Priors with Language Models for Combinatorial Optimization** NeurIPS, 2025. [paper](https://arxiv.org/pdf/2506.11057)

7. **OPT-BENCH: Evaluating LLM Agent on Large-Scale Search Spaces Optimization Problems** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.10764), [code](https://github.com/OliverLeeXZ/OPT-BENCH)

8. **DaSAThco: Data-Aware SAT Heuristics Combinations Optimization via Large Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.12602)

9. **CP-Bench: Evaluating Large Language Models for Constraint Modelling** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.06052)

10. **AutoPBO: LLM-powered Optimization for Local Search PBO Solvers** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.04007)

11. **Autonomous Code Evolution MeetsNP-Completeness** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.07367)

12. **Automatically discovering heuristics in a complex SAT solver with large language models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2507.22876)

13. **Towards a Generic Representation of Combinatorial Problems for Learning-Based Approaches** CPAIOR, 2024. [paper](https://arxiv.org/pdf/2403.06026), [code](https://github.com/corail-research/learning-generic-csp)

14. **QUBE: Enhancing Automatic Heuristic Design via Quality-Uncertainty Balanced Evolution** Arxiv, 2024. [paper](https://arxiv.org/pdf/2412.20694), [code](https://github.com/zzjchen/QUBE_code)

15. **Foundation Models for Boolean Logic** Under Review, 2024. [paper](https://openreview.net/forum?id=qeY25DwmKO)

16. **Efficient Combinatorial Optimization via Heat Diffusion** NeurIPS, 2024. [paper](https://openreview.net/forum?id=psDrko9v1D), [code](https://github.com/AwakerMhy/HeO)
    *Hengyuan Ma, Wenlian Lu, Jianfeng Feng*

17. **Distributed Constrained Combinatorial Optimization leveraging Hypergraph Neural Networks** Nature Machine Intelligence, 2024. [paper](https://arxiv.org/abs/2311.09375), [code](https://github.com/nasheydari/HypOp)
    *Nasimeh Heydaribeni, Xinrui Zhan, Ruisi Zhang, Tina Eliassi-Rad, Farinaz Koushanfar*

18. **AutoSAT: Automatically Optimize SAT Solvers via Large Language Models** Arxiv, 2024. [paper](https://arxiv.org/pdf/2402.10705)

19. **Let the Flows Tell: Solving Graph Combinatorial Optimization Problems with GFlowNets** NeurlPS, 2023. [paper](https://arxiv.org/abs/2305.17010), [code](https://github.com/zdhNarsil/GFlowNet-CombOpt)
    *Dinghuai Zhang, Hanjun Dai, Nikolay Malkin, Aaron Courville, Yoshua Bengio, Ling Pan*

20. **HardSATGEN: Understanding the Difficulty of Hard SAT Formula Generation and A Strong Structure-Hardness-Aware Baseline** KDD, 2023. [paper](https://dl.acm.org/doi/10.1145/3580305.3599837), [code](https://github.com/Thinklab-SJTU/HardSATGEN)
    *Yang Li, Xinyan Chen, Wenxuan Guo, Xijun Li, Wanqian Luo, Junhua Huang, Hui-Ling Zhen, Mingxuan Yuan, Junchi Yan*

21. **SATformer: Transformers for SAT Solving.** Arxiv, 2022. [paper](https://arxiv.org/abs/2209.00953)
    *Zhengyuan Shi, Sadaf Khan Min Li, Mingxuan Yuan Hui-Ling Zhen, Qiang Xu.*

22. **Optimistic tree search strategies for black-box combinatorial optimization** NeurlPS, 2022. [paper](https://openreview.net/forum?id=JGLW4DvX11F)
    *Cedric Malherbe, Antoine Grosnit, Rasul Tutunov, Haitham Bou Ammar, Jun Wang*

23. **One Model, Any CSP: Graph Neural Networks as Fast Global Search Heuristics for Constraint Satisfaction** IJCAI, 2022. [paper](https://arxiv.org/pdf/2208.10227), [code](https://github.com/toenshoff/ANYCSP)

24. **On the Performance of Deep Generative Models of Realistic SAT Instances.** SAT, 2022. [paper](https://drops.dagstuhl.de/opus/volltexte/2022/16677/pdf/LIPIcs-SAT-2022-3.pdf)
    *Iván, Pablo Mesejo Garzón, Jesús Giráldez-Cru.*

25. **NSNet: A General Neural Probabilistic Framework for Satisfiability Problems** NeurIPS, 2022. [paper](https://arxiv.org/abs/2211.03880)
    *Zhaoyu Li, Xujie Si*

26. **NeuroComb: Improving SAT Solving with Graph Neural Networks.** Arxiv, 2022. [paper](https://arxiv.org/abs/2110.14053)
    *Wenxi Wang, Mohit Tiwari Yang Hu, Kenneth McMillan Sarfraz Khurshid, Risto Miikkulainen.*

27. **Neural Set Function Extensions: Learning with Discrete Functions in High Dimensions** NeurIPS, 2022. [paper](https://arxiv.org/abs/2208.04055)
    *Nikolaos Karalias, Joshua Robinson, Andreas Loukas, Stefanie Jegelka*

28. **Goal-Aware Neural SAT Solver.** IJCNN, 2022. [paper](https://ieeexplore.ieee.org/document/9892733)
    *Emils Ozolins, Andis Draguns Karlis Freivalds, Ronalds Zakovskis Eliza Gaile, Sergejs Kozlovics.*

29. **Generalization of Neural Combinatorial Solvers Through the Lens of Adversarial Robustness** ICLR, 2022. [paper](https://openreview.net/forum?id=vJZ7dPIjip3)
    *Simon Geisler, Johanna Sommer, Jan Schuchardt, Aleksandar Bojchevski, Stephan Günnemann*

30. **DeepSAT: An EDA-Driven Learning Framework for SAT.** Arxiv, 2022. [paper](http://arxiv.org/abs/2205.13745)
    *Min, Zhengyuan Shi, Qiuxia Lai, Sadaf Khan Li, Qiang Xu.*

31. **Augment with Care: Contrastive Learning for Combinatorial Problems.** ICML, 2022. [paper](https://proceedings.mlr.press/v162/duan22b.html), [code](https://github.com/h4duan/contrastive-sat)
    *Haonan, Pashootan Vaezipoor, Max B. Paulus, Yangjun Ruan Duan, Chris J. Maddison*

32. **Predicting Propositional Satisfiability via End-to-End Learning.** AAAI, 2020. [paper](https://ojs.aaai.org/index.php/AAAI/article/download/5733/5589)
    *Chris Cameron, Jason Hartford Rex Chen, Kevin Leyton-Brown.*

33. **Online Bayesian Moment Matching based SAT Solver Heuristics.** ICML, 2020. [paper](http://proceedings.mlr.press/v119/duan20c/duan20c.pdf), [code](https://github.com/saeednj/BMMSAT)
    *Haonan, Saeed Nejati, George Trimponias, Pascal Poupart Duan, Vijay Ganesh.*

34. **NLocalSAT: Boosting Local Search with Solution Prediction.** Arxiv, 2020. [paper](https://arxiv.org/pdf/2001.09398), [code](https://github.com/myxxxsquared/NLocalSAT)
    *Wenjie, Zeyu Sun, Qihao Zhu, Ge Li, Shaowei Cai, Yingfei Xiong Zhang, Lu Zhang.*

35. **Neural heuristics for SAT solving.** Arxiv, 2020. [paper](https://arxiv.org/pdf/2005.13406)
    *Sebastian, Michał Łuszczyk Jaszczur, Henryk Michalewski.*

36. **Learning Clause Deletion Heuristics with Reinforcement Learning.** AITP, 2020. [paper](http://aitp-conference.org/2020/abstract/paper_25.pdf)
    *Pashootan, Gil Lederman, Yuhuai Wu, Roger Grosse Vaezipoor, Fahiem Bacchus.*

37. **Enhancing SAT solvers with glue variable predictions.** Arxiv, 2020. [paper](https://arxiv.org/pdf/2007.02559)
    *Jesse Michael. Han*

38. **Classification of SAT problem instances by machine learning methods.** CEUR, 2020. [paper](http://ceur-ws.org/Vol-2650/paper11.pdf)
    *Márk, Zijian Győző Yang Danisovszky, Gábor Kusper.*

39. **Can Q-Learning with Graph Networks Learn a Generalizable Branching Heuristic for a SAT Solver?** NeurIPS, 2020. [paper](http://www.cs.ox.ac.uk/people/shimon.whiteson/pubs/kurinnips20.pdf)
    *Shimon Whiteson*

40. **Learning to solve circuit-SAT: An unsupervised differentiable approach.** ICLR, 2019. [paper](https://openreview.net/pdf?id=BJxgz2R9t7), [code](https://github.com/johannaSommer/generalization-neural-co-solvers)
    *Saeed, Sergiy Matusevych Amizadeh, Markus Weimer.*

41. **Learning Local Search Heuristics for Boolean Satisfiability.** NeurIPS, 2019. [paper](https://www.cs.cmu.edu/~eyolcu/papers/learning-local-search-heuristics-sat.pdf), [code](https://github.com/emreyolcu/sat)
    *Emre Yolcu, Barnabas Poczos*

42. **Learning Heuristics for Quantified Boolean Formulas through Reinforcement Learning.** Arxiv, 2019. [paper](https://arxiv.org/pdf/1807.08058), [code](https://github.com/lederg/learningqbf)
    *Gil Lederman, Edward A. Lee Markus N. Rabe, Sanjit A. Seshia.*

43. **Improving SAT solver heuristics with graph networks and reinforcement learning.** Arxiv, 2019. [paper](https://arxiv.org/pdf/1909.11830)
    *Vitaly Kurin, Shimon Whiteson Saad Godil, Bryan Catanzaro.*

44. **Guiding high-performance SAT solvers with unsat-core predictions.** SAT, 2019. [paper](https://arxiv.org/pdf/1903.04671)
    *Daniel Selsam, Nikolaj Bjørner.*

45. **Graph neural reasoning may fail in certifying boolean unsatisfiability.** Arxiv, 2019. [paper](https://arxiv.org/pdf/1909.11588)
    *Ziliang Chen, Zhanfu Yang.*

46. **G2SAT: Learning to Generate SAT Formulas.** NeurIPS, 2019. [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7138247/), [code](https://github.com/JiaxuanYou/G2SAT)
    *Jiaxuan, Haoze Wu, Clark Barrett, Raghuram Ramanujan You, Jure Leskovec.*

47. **Machine learning-based restart policy for CDCL SAT solvers.** SAT, 2018. [paper](http://www.t-news.cn/Floc2018/FLoC2018-pages/proceedings_paper_477.pdf)
    *Jia Hui Liang, Minu Mathew Chanseok Oh, Chunxiao Li Ciza Thomas, Vijay Ganesh.*

48. **Learning a SAT solver from single-bit supervision.** Arxiv, 2018. [paper](https://arxiv.org/pdf/1802.03685), [code](https://github.com/dselsam/neurosat)
    *Daniel Selsam, Benedikt Bünz Matthew Lamm, Leonardo de Moura Percy Liang, David L. Dill.*

49. **Graph neural networks and boolean satisfiability.** Arxiv, 2017. [paper](https://arxiv.org/pdf/1702.03592)
    *Benedikt Bünz, Matthew Lamm.*

### [Computing Resource Allocation](#content) · *6 papers*

1. **A Two-stage Framework and Reinforcement Learning-based Optimization Algorithms for Complex Scheduling Problems** Arxiv, 2021. [paper](https://arxiv.org/abs/2103.05847)
    *Yongming He, Guohua Wu, Yingwu Chen, Witold Pedrycz*

2. **A Bi-Level Framework for Learning to Solve Combinatorial Optimization on Graphs** NeurIPS, 2021. [paper](https://arxiv.org/abs/2106.04927), [code](https://github.com/Thinklab-SJTU/PPO-BiHyb)
    *Runzhong Wang, Zhigang Hua, Gan Liu, Jiayi Zhang, Junchi Yan, Feng Qi, Shuang Yang, Jun Zhou, Xiaokang Yang*

3. **Smart Resource Allocation for Mobile Edge Computing: A Deep Reinforcement Learning Approach** IEEE Transactions on Emerging Topics in Computing, 2019. [paper](https://ieeexplore.ieee.org/abstract/document/8657791)
    *Lei Zhao Jiadai, Nei Kato Jiajia Liu*

4. **Learning to Perform Local Rewriting for Combinatorial Optimization.** NeurIPS, 2019. [paper](https://arxiv.org/abs/1810.00337), [code](https://github.com/facebookresearch/neural-rewriter)
    *Xinyun Chen, Yuandong Tian*

5. **Learning Scheduling Algorithms for Data Processing Clusters** SIGCOMM, 2019. [paper](https://static.aminer.cn/storage/pdf/arxiv/18/1810/1810.01963.pdf), [code](https://github.com/hongzimao/decima-sim)
    *Hongzi Mao, Malte Schwarzkopf, Bojja Shaileshh Venkatakrishnan, Zili Meng, Mohammad Alizadeh*

6. **Resource Management with Deep Reinforcement Learning.** HotNets, 2016. [paper](https://dl.acm.org/doi/abs/10.1145/3005745.3005750)
    *Hongzi Mao, Mohammad Alizadeh, Ishai Menache, Srikanth Kandula*

### [Bin Packing Problem](#content) · *60 papers*

1. **Rethinking LLM-Driven Heuristic Design: Generating Efficient and Specialized Solvers via Dynamics-Aware Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.20868)

2. **PathWise: Planning through World Model for Automated Heuristic Design via Self-Evolving LLMs** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.20539)

3. **Generalizable Heuristic Generation Through LLMs with Meta-Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2505.20881), [code](https://github.com/yiding-s/MoH)
    *Yiding Shi, Jianan Zhou, Wen Song, Jieyi Bi, Yaoxin Wu, Zhiguang Cao, Jie Zhang*

4. **Game-Theoretic Co-Evolution for LLM-Based Heuristic Discovery** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.22896)

5. **EoH-S: Evolution of Heuristic Set using LLMs for Automated Heuristic Design** AAAI, 2026. [paper](https://arxiv.org/abs/2508.03082), [code](https://github.com/FeiLiu36/EoH-S)
    *Fei Liu, Yilu Liu, Qingfu Zhang, Xialiang Tong, Mingxuan Yuan*

6. **DRAGON: LLM-Driven Decomposition and Reconstruction Agents for Large-Scale Combinatorial Optimization** AAMAS, 2026. [paper](https://arxiv.org/abs/2601.06502)
    *Shengkai Chen, Zhiguang Cao, Jianan Zhou, Yaoxin Wu, Senthilnath Jayavelu, Zhuoyi Lin, Xiaoli Li, Shili Xiang*

7. **CDEoH: Category-Driven Automatic Algorithm Design With Large Language Models** Arxiv, 2026. [paper](https://arxiv.org/pdf/2603.19284)

8. **Beyond the Node: Clade-level Selection for Efficient MCTS in Automatic Heuristic Design** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.00549)

9. **X-evolve: Solution space evolution powered by large language models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2508.07932)

10. **RoCo: Role-Based LLMs Collaboration for Automatic Heuristic Design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.03762)

11. **RedAHD: Reduction-Based End-to-End Automatic Heuristic Design with Large Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2505.20242)

12. **MOTIF: Multi-strategy Optimization via Turn-based Interactive Framework** AAAI, 2025. [paper](https://arxiv.org/abs/2508.03929), [code](https://github.com/HaiAu2501/MOTIF)

13. **Monte Carlo Tree Search for Comprehensive Exploration in LLM-Based Automatic Heuristic Design** ICML, 2025. [paper](https://arxiv.org/pdf/2501.08603), [code](https://github.com/zz1358m/MCTS-AHD-master)

14. **MeLA: A Metacognitive LLM-Driven Architecture for Automatic Heuristic Design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2507.20541), [code](https://github.com/Qzs1335/MeLA)

15. **LLM-Driven Instance-Specific Heuristic Generation and Selection** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.00490)

16. **irace-evo: Automatic Algorithm Configuration Extended With LLM-Based Code Evolution** Arxiv, 2025. [paper](https://arxiv.org/pdf/2511.14794)

17. **HIFO-PROMPT: Prompting with Hindsight and Foresight For LLM-Based Automatic Heuristic Design** ICLR, 2025. [paper](https://arxiv.org/pdf/2508.13333)

18. **Hierarchical Representations for Cross-task Automated Heuristic Design using LLMs** Under Review, 2025. [paper](https://openreview.net/pdf?id=dgvx86qybJ)

19. **Fitness Landscape of Large Language Model-Assisted Automated Algorithm Search** Arxiv, 2025. [paper](https://arxiv.org/pdf/2504.19636)

20. **Experience-guided reflective co-evolution of prompts and heuristics for automatic algorithm design** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.24509)

21. **Experience-Guided Reflective Co-Evolution of Prompts and Heuristics for Automatic Algorithm Design** Under Review, 2025. [paper](https://openreview.net/pdf?id=oD9RwlFqEE)

22. **Efficient Heuristics Generation for Solving Combinatorial Optimization Problems Using Large Language Models** KDD, 2025. [paper](https://arxiv.org/pdf/2505.12627v1), [code](https://github.com/wuuu110/Hercules)

23. **Cognitively Inspired Reflective Evolution: Interactive Multi-Turn LLM–EA Synthesis of Heuristics for Combinatorial Optimization** Under Review, 2025. [paper](https://openreview.net/pdf?id=31VTD5pS2v)

24. **Code Evolution Graphs: Understanding Large Language Model Driven Design of Algorithms** GECCO, 2025. [paper](https://arxiv.org/pdf/2503.16668)

25. **CALM: Co-evolution of Algorithms and Language Model for Automatic Heuristic Design** ICLR, 2025. [paper](https://arxiv.org/pdf/2505.12285v1)

26. **Algorithm Discovery With LLMs: Evolutionary Search Meets Reinforcement Learning** COLM, 2025. [paper](https://arxiv.org/pdf/2504.05108)

27. **Adversarial examples for heuristics in combinatorial optimization: An LLM based approach** Under Review, 2025. [paper](https://openreview.net/pdf?id=fasU6t3hL4)

28. **ACCORD: Autoregressive Constraint-satisfying Generation for COmbinatorial Optimization with Routing and Dynamic attention** Under Review, 2025. [paper](https://openreview.net/pdf?id=f0TBAdcJ8m)

29. **Self-Guiding Exploration for Combinatorial Problems** NeurIPS, 2024. [paper](https://arxiv.org/pdf/2405.17950), [code](https://github.com/Zangir/LLM-for-CP)

30. **ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution** NeurIPS, 2024. [paper](https://arxiv.org/pdf/2402.01145), [code](https://github.com/ai4co/reevo)

31. **QUBE: Enhancing Automatic Heuristic Design via Quality-Uncertainty Balanced Evolution** Arxiv, 2024. [paper](https://arxiv.org/pdf/2412.20694), [code](https://github.com/zzjchen/QUBE_code)

32. **Multi-objective Evolution of Heuristic Using Large Language Model** AAAI, 2024. [paper](https://arxiv.org/pdf/2409.16867)

33. **HSEvo: Elevating Automatic Heuristic Design with Diversity-Driven Harmony Search and Genetic Algorithm Using LLMs** AAAI, 2024. [paper](https://arxiv.org/pdf/2412.14995), [code](https://github.com/datphamvn/HSEvo)

34. **Evolution of Heuristics: Towards Efficient Automatic Algorithm Design Using Large Language Model** ICML, 2024. [paper](https://arxiv.org/pdf/2401.02051), [code](https://github.com/FeiLiu36/EoH)

35. **A Neural Column Generation Approach to the Vehicle Routing Problem with Two-Dimensional Loading and Last-In-First-Out Constraints** IJCAI, 2024. [paper](https://www.ijcai.org/proceedings/2024/0218.pdf), [code](https://github.com/xyfffff/NCG-for-2L-CVRP)
    *Yifan Xia, Xiangyi Zhang*

36. **Mathematical discoveries from program search with large language models** Nature, 2023. [paper](https://www.nature.com/articles/s41586-023-06924-6), [code](https://github.com/google-deepmind/funsearch)

37. **Improved Algorithms for Multi-period Multi-class Packing Problemswith Bandit Feedback** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/24252)
    *Wonyoung Kim, Garud Iyengar, Assaf Zeevi*

38. **Adjustable Robust Reinforcement Learning for Online 3D Bin Packing** NeurIPS, 2023. [paper](https://openreview.net/forum?id=1mdTYi1jAW)
    *Yuxin Pan, Yize Chen, Fangzhen Lin*

39. **Learning Efficient Online 3D Bin Packing on Packing Configuration Trees.** ICLR, 2022. [paper](https://openreview.net/forum?id=bfuGjlCwAq)
    *Hang Zhao, Kai Xu*

40. **Solving 3D bin packing problem via multimodal deep reinforcement learning** AAMAS, 2021. [paper](https://www.ifaamas.org/Proceedings/aamas2021/pdfs/p1548.pdf)
    *Yuan, Zhiguang Cao Jiang, Jie Zhang*

41. **Online 3D Bin Packing with Constrained Deep Reinforcement Learning.** AAAI, 2021. [paper](https://arxiv.org/abs/2006.14978), [code](https://github.com/alexfrom0815/Online-3D-BPP-DRL)
    *Hang Zhao, Qijin She, Chenyang Zhu, Yin Yang, Kai Xu*

42. **Learning to Solve 3-D Bin Packing Problem via Deep Reinforcement Learning and Constraint Programming** IEEE transactions on cybernetics, 2021. [paper](https://ieeexplore.ieee.org/document/9606618/)
    *Yuan Jiang, Zhiguang Cao, Jie Zhang*

43. **Learning to Pack: A Data-Driven Tree Search Algorithm for Large-Scale 3D Bin Packing Problem** CIKM, 2021. [paper](https://dl.acm.org/doi/abs/10.1145/3459637.3481933)
    *Qianwen Zhu, Xihan Li, Zihan Zhang, Zhixing Luo, Xialiang Tong, Mingxuan Yuan, Jia Zeng*

44. **Learning Practically Feasible Policies for Online 3D Bin Packing** Arxiv, 2021. [paper](https://arxiv.org/abs/2108.13680)
    *Hang Zhao, Chenyang Zhu, Xin Xu, Hui Huang, Kai Xu*

45. **Attend2Pack: Bin Packing through Deep Reinforcement Learning with Attention** ICML Workshop, 2021. [paper](https://arxiv.org/abs/2107.04333)
    *Jingwei Zhang, Bin Zi, Xiaoyu Ge*

46. **TAP-Net: Transport-and-Pack using Reinforcement Learning.** TOG, 2020. [paper](https://dl.acm.org/doi/abs/10.1145/3414685.3417796), [code](https://github.com/Juzhan/TAP-Net)
    *Ruizhen Hu, Juzhan Xu, Bin Chen, Minglun Gong, Hao Zhang, Hui Huang*

47. **Simultaneous Planning for Item Picking and Placing by Deep Reinforcement Learning** IROS, 2020. [paper](http://ras.papercept.net/images/temp/IROS/files/0330.pdf)
    *Tatsuya Tanaka, Toshimitsu Kaneko, Masahiro Sekine, Voot Tangkaratt, Masashi Sugiyama*

48. **Robot Packing with Known Items and Nondeterministic Arrival Order.** TASAE, 2020. [paper](https://ieeexplore.ieee.org/abstract/document/9205914/)
    *Fan Wang, Kris Hauser*

49. **PackIt: A Virtual Environment for Geometric Planning** ICML, 2020. [paper](http://proceedings.mlr.press/v119/goyal20b.html), [code](https://github.com/princeton-vl/PackIt)
    *Ankit Goyal, Jia Deng*

50. **Monte Carlo Tree Search on Perfect Rectangle Packing Problem Instances** GECCO, 2020. [paper](https://dl.acm.org/doi/abs/10.1145/3377929.3398115)
    *Igor Pejic, Daan van den Berg*

51. **A Generalized Reinforcement Learning Algorithm for Online 3D Bin-Packing.** AAAI Workshop, 2020. [paper](https://arxiv.org/abs/2007.00463)
    *Richa Verma, Aniruddha Singhal, Harshad Khadilkar, Ansuma Basumatary, Siddharth Nayak, Harsh Vardhan Singh, Swagat Kumar, Rajesh Sinha*

52. **Solving Packing Problems by Conditional Query Learning** OpenReview, 2019. [paper](https://openreview.net/forum?id=BkgTwRNtPB)
    *Dongda Li, Changwei Ren, Zhaoquan Gu, Yuexuan Wang, Francis Lau*

53. **RePack: Dense Object Packing Using Deep CNN with Reinforcement Learning** CACS, 2019. [paper](https://ieeexplore.ieee.org/abstract/document/9024360/?casa_token=ScXezdDDiwMAAAAA:fglP_vbiQUJgLZcM7YZyqnDh_qA8jOjIh-zbH7ru0XSVBghh8OAxpThOU3BqhBeet4NlSrdHPcU)
    *Yu-Cheng Chu, Horng-Horng Lin*

54. **Reinforcement learning driven heuristic optimization** Arxiv, 2019. [paper](https://arxiv.org/pdf/1906.06639.pdf)
    *Qingpeng Cai, Will Hang, Azalia Mirhoseini, George Tucker, Jingtao Wang, Wei Wei*

55. **A Multi-task Selected Learning Approach for Solving 3D Bin Packing Problem.** AAMAS, 2019. [paper](https://arxiv.org/abs/1804.06896)
    *Lu Duan, Haoyuan Hu, Yu Qian, Yu Gong, Xiaodong Zhang, Yinghui Xu, Jiangwen Wei*

56. **A Data-Driven Approach for Multi-level Packing Problems in Manufacturing Industry** KDD, 2019. [paper](https://dl.acm.org/doi/abs/10.1145/3292500.3330708)
    *Lei Chen, Xialiang Tong, Mingxuan Yuan, Jia Zeng, Lei Chen*

57. **Ranked Reward: Enabling Self-Play Reinforcement Learning for Combinatorial Optimization Alexandre** Arxiv, 2018. [paper](https://arxiv.org/abs/1807.01672)
    *Alexandre Laterre, Yunguan Fu, Mohamed Khalil Jabri, Alain-Sam Cohen, David Kas, Karl Hajjar, Torbjorn S Dahl, Amine Kerkeni, Karim Beguir*

58. **Best Arm Identification in Multi-armed Bandits with Delayed Feedback** PMLR, 2018. [paper](http://proceedings.mlr.press/v84/grover18b.html)
    *Aditya Grover, Todor Markov, Peter Attia, Norman Jin, Nicolas Perkins, Bryan Cheong, Michael Chen, Zi Yang, Stephen Harris, William Chueh, others*

59. **Solving a New 3D Bin Packing Problem with Deep Reinforcement Learning Method** Arxiv, 2017. [paper](https://arxiv.org/abs/1708.05930)
    *Haoyuan Hu, Xiaodong Zhang, Xiaowei Yan, Longfei Wang, Yinghui Xu*

60. **Small Boxes Big Data: A Deep Learning Approach to Optimize Variable Sized Bin Packing** BigDataService, 2017. [paper](https://ieeexplore.ieee.org/abstract/document/7944923/?casa_token=mRzI_XBy3ycAAAAA:yD9Le2KBNq1TMpW_1etb0RF-oFVcLJj9Up0Z2qI6XJmA-UffxxSZRIx7RklaQED-yXwuwBC4M_w)
    *Feng Mao, Edgar Blanco, Mingang Fu, Rohit Jain, Anurag Gupta, Sebastien Mancel, Rong Yuan, Stephen Guo, Sai Kumar, Yayang Tian*

### [Graph Edit Distance](#content) · *8 papers*

1. **Gelato: Graph Edit Distance via Autoregressive Neural Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=6ZTcLNmguc), [code](https://github.com/BorgwardtLab/Gelato)
    *Paolo Pellizzoni, Till Hendrik Schulz, Karsten Borgwardt*

2. **GraphArena: Evaluating and Exploring Large Language Models on Graph Computation** ICLR, 2025. [paper](https://openreview.net/pdf?id=Y1r9yCMzeA), [code](https://github.com/squareRoot3/GraphArena/tree/master)

3. **Combinatorial Learning of Graph Edit Distance via Dynamic Embedding.** CVPR, 2021. [paper](https://arxiv.org/abs/2011.15039), [code](https://github.com/Thinklab-SJTU/GENN-Astar)
    *Runzhong Wang, Tianqi Zhang, Tianshu Yu, Junchi Yan, Xiaokang Yang*

4. **A Bi-Level Framework for Learning to Solve Combinatorial Optimization on Graphs** NeurIPS, 2021. [paper](https://arxiv.org/abs/2106.04927), [code](https://github.com/Thinklab-SJTU/PPO-BiHyb)
    *Runzhong Wang, Zhigang Hua, Gan Liu, Jiayi Zhang, Junchi Yan, Feng Qi, Shuang Yang, Jun Zhou, Xiaokang Yang*

5. **Learning-Based Efficient Graph Similarity Computation via Multi-Scale Convolutional Set Matching** AAAI, 2020. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/5720), [code](https://github.com/yunshengb/GraphSim)
    *Yunsheng Bai, Hao Ding, Ken Gu, Yizhou Sun, Wei Wang*

6. **Convolutional Embedding for Edit Distance** SIGIR, 2020. [paper](https://dl.acm.org/doi/abs/10.1145/3397271.3401045), [code](https://github.com/xinyandai/string-embed)
    *Xinyan Dai, Xiao Yan, Kaiwen Zhou, Yuxuan Wang, Han Yang, James Cheng*

7. **SimGNN - A Neural Network Approach to Fast Graph Similarity Computation** WSDM, 2019. [paper](https://arxiv.org/abs/1808.05689), [code](https://github.com/yunshengb/SimGNN)
    *Yunsheng Bai, Hao Ding, Song Bian, Ting Chen, Yizhou Sun, Wei Wang*

8. **Graph Matching Networks for Learning the Similarity of Graph Structured Objects** ICML, 2019. [paper](https://arxiv.org/abs/1904.12787), [code](https://github.com/Lin-Yijie/Graph-Matching-Networks)
    *Yujia Li, Chenjie Gu, Thomas Dullien, Oriol Vinyals, Pushmeet Kohli*

### [Hamiltonian Cycle Problem](#content) · *3 papers*

1. **VSAL: A Vision Solver with Adaptive Layouts for Graph Property Detection** WWW, 2026. [paper](https://arxiv.org/abs/2602.13880), [code](https://github.com/Jiahao-Xie-86/VSAL)
    *Jiahao Xie, Guangmo Tong*

2. **UniCO: On Unified Combinatorial Optimization via Problem Reduction to Matrix-Encoded General TSP** ICLR, 2025. [paper](https://openreview.net/forum?id=yEwakMNIex), [code](https://github.com/Thinklab-SJTU/UniCO)
    *Wenzheng Pan, Hao Xiong, Jiale Ma, Wentao Zhao, Yang Li, Junchi Yan*

3. **A Bi-Level Framework for Learning to Solve Combinatorial Optimization on Graphs** NeurIPS, 2021. [paper](https://arxiv.org/abs/2106.04927), [code](https://github.com/Thinklab-SJTU/PPO-BiHyb)
    *Runzhong Wang, Zhigang Hua, Gan Liu, Jiayi Zhang, Junchi Yan, Feng Qi, Shuang Yang, Jun Zhou, Xiaokang Yang*

### [Graph Coloring](#content) · *9 papers*

1. **OPT-BENCH: Evaluating LLM Agent on Large-Scale Search Spaces Optimization Problems** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.10764), [code](https://github.com/OliverLeeXZ/OPT-BENCH)

2. **Behavior and Representation in Large Language Models for Combinatorial Optimization: From Feature Extraction to Algorithm Selection** Arxiv, 2025. [paper](https://arxiv.org/pdf/2512.13374)

3. **AutoMOAE: Multi-Objective Auto-Algorithm Evolution** Under Review, 2025. [paper](https://openreview.net/pdf?id=G8tP1Z9dLy)

4. **Towards a Generic Representation of Combinatorial Problems for Learning-Based Approaches** CPAIOR, 2024. [paper](https://arxiv.org/pdf/2403.06026), [code](https://github.com/corail-research/learning-generic-csp)

5. **NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes** ACL, 2023. [paper](https://arxiv.org/pdf/2312.14890), [code](https://github.com/casmlab/NPHardEval)

6. **Learning to Generate Columns with Application to Vertex Coloring** ICLR, 2023. [paper](https://openreview.net/forum?id=JHW30A4DXtO), [code](https://github.com/yuansuny/mlcg)
    *Yuan Sun, Andreas T Ernst, Xiaodong Li, Jake Weiner*

7. **Neural Models for Output-Space Invariance in Combinatorial Problems** ICLR, 2022. [paper](https://openreview.net/forum?id=ibrUkC-pbis)
    *Yatin Nandwani, Vidit Jain, Parag Singla, others*

8. **Enhancing Column Generation by a Machine-Learning-Based Pricing Heuristic for Graph Coloring** AAAI, 2022. [paper](https://www.aaai.org/AAAI22Papers/AAAI-4026.ShenY.pdf), [code](https://github.com/Joey-Shen/MLPH.git)
    *Yunzhuang, Yuan Sun, Xiaodong Li, Andrew Craig Eberhard Shen, Andreas T. Ernst.*

9. **Deep Learning-based Hybrid Graph-Coloring Algorithm for Register Allocation.** Arxiv, 2019. [paper](https://arxiv.org/abs/1912.03700)
    *Dibyendu Das, Shahid Asghar Ahmad, Kumar Venkataramanan*

### [Maximal Common Subgraph](#content) · *3 papers*

1. **OPT-BENCH: Evaluating LLM Agent on Large-Scale Search Spaces Optimization Problems** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.10764), [code](https://github.com/OliverLeeXZ/OPT-BENCH)

2. **GraphArena: Evaluating and Exploring Large Language Models on Graph Computation** ICLR, 2025. [paper](https://openreview.net/pdf?id=Y1r9yCMzeA), [code](https://github.com/squareRoot3/GraphArena/tree/master)

3. **Fast Detection of Maximum Common Subgraph via Deep Q-Learning.** Arxiv, 2020. [paper](https://arxiv.org/abs/2002.03129)
    *Yunsheng Bai, Derek Xu, Alex Wang, Ken Gu, Xueqing Wu, Agustin Marinovic, Christopher Ro, Yizhou Sun, Wei Wang*

### [Influence Maximization](#content) · *7 papers*

1. **Can Large Language Models Be Trusted as Black-Box Evolutionary Optimizers for Combinatorial Problems?** Arxiv, 2025. [paper](https://arxiv.org/pdf/2501.15081)

2. **Bridging Visualization and Optimization: Multimodal Large Language Models on Graph-Structured Combinatorial Optimization** Arxiv, 2025. [paper](https://arxiv.org/pdf/2501.11968)

3. **Towards One-shot Neural Combinatorial Solvers: Theoretical and Empirical Notes on the Cardinality-Constrained Case** ICLR, 2023. [paper](https://openreview.net/forum?id=h21yJhdzbwz), [code](https://github.com/Thinklab-SJTU/One-Shot-Cardinality-NN-Solver)
    *Runzhong Wang, Li Shen, Yiting Chen, Junchi Yan, Xiaokang Yang, Dacheng Tao*

4. **Deep Graph Representation Learning and Optimization for Influence Maximization** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/24512)
    *Chen Ling, Junji Jiang, Junxiang Wang, My T. Thai, Lukas Xue, James Song, Meikang Qiu, Liang Zhao*

5. **LeNSE: Learning To Navigate Subgraph Embeddings for Large-Scale Combinatorial Optimisation** ICML, 2022. [paper](https://proceedings.mlr.press/v162/ireland22a.html), [code](https://github.com/davidireland3/LeNSE)
    *David Ireland, G. Montana*

6. **Controlling Graph Dynamics with Reinforcement Learning and Graph Neural Networks.** ICML, 2021. [paper](https://arxiv.org/abs/2010.05313)
    *Eli A. Meirom, Haggai Maron, Shie Mannor, Gal Chechik*

7. **Learning Heuristics over Large Graphs via Deep Reinforcement Learning.** NeurIPS, 2020. [paper](https://arxiv.org/abs/1903.03332)
    *Akash Mittal, Anuj Dhawan, Sahil Manchanda, Sourav Medya, Sayan Ranu, Ambuj Singh*

### [Max Clique](#content) · *10 papers*

1. **ConRep4CO: Contrastive Representation Learning of Combinatorial Optimization Instances across Types** ICLR, 2026. [paper](https://openreview.net/forum?id=OXRnvOOiAf), [code](https://github.com/Thinklab-SJTU/ConRep4CO)
    *Ziao Guo, Yang Li, Shiyue Wang, Junchi Yan*

2. **Scalable Discrete Diffusion Samplers: Combinatorial Optimization and Statistical Physics** ICLR, 2025. [paper](https://openreview.net/pdf?id=peNgxpbdxB)
    *Sebastian Sanokowski, Wilhelm Franz Berghammer, Haoyu Peter Wang, Martin Ennemoser, Sepp Hochreiter, Sebastian Lehner*

3. **ML4CO-Bench-101: Benchmark Machine Learning for Classic Combinatorial Problems on Graphs** NeurIPS, 2025. [paper](https://openreview.net/forum?id=ye4ntB1Kzi), [code](https://github.com/Thinklab-SJTU/ML4CO-Bench-101)
    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

4. **COExpander: Adaptive Solution Expansion for Combinatorial Optimization** ICML, 2025. [paper](https://openreview.net/forum?id=KMaBXMWsBM), [code](https://github.com/Thinklab-SJTU/COExpander)
    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

5. **Approximation algorithms for combinatorial optimization with predictions** ICLR, 2025. [paper](https://openreview.net/forum?id=AEFVa6VMu1)
    *Antonios Antoniadis, Marek Elias, Adam Polak, Moritz Venzin*

6. **A Diffusion Model Framework for Unsupervised Neural Combinatorial Optimization** ICML, 2024. [paper](https://arxiv.org/abs/2406.01661), [code](https://github.com/ml-jku/DIffUCO)
    *Sebastian Sanokowski, Sepp Hochreiter, Sebastian Lehner*

7. **Variational Annealing on Graphs for Combinatorial Optimization** NeurlPS, 2023. [paper](https://openreview.net/forum?id=SLx7paoaTU), [code](https://github.com/ml-jku/VAG-CO)
    *Sebastian Sanokowski, Wilhelm Franz Berghammer, Sepp Hochreiter, Sebastian Lehner*

8. **Learning fine-grained search space pruning and heuristics for combinatorial optimization.** Journal of Heuristics, 2023. [paper](https://dx.doi.org/10.1007/s10732-023-09512-z)
    *Juho Lauri, Sourav Dutta, Marco Grassia, Deepak Ajwani*

9. **DISCS: A Benchmark for Discrete Sampling** NeurlPS, 2023. [paper](https://openreview.net/forum?id=oi1MUMk5NF), [code](https://github.com/google-research/discs)
    *Katayoon Goshvadi, Haoran Sun, Xingchao Liu, Azade Nova, Ruqi Zhang, Will Sussman Grathwohl, Dale Schuurmans, Hanjun Dai*

10. **Can Hybrid Geometric Scattering Networks Help Solve the Maximum Clique Problem** NeurIPS, 2022. [paper](https://openreview.net/forum?id=uxc8hDSs_xh), [code](https://github.com/yimengmin/geometricscatteringmaximalclique)
    *Yimeng Min, Frederik Wenkel, Michael Perlmutter, Guy Wolf*

### [Mixed Integer Programming](#content) · *101 papers*

1. **Reasoning in a Combinatorial and Constrained World: Benchmarking LLMs on Natural-Language Combinatorial Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.02188)

2. **OR-Agent: Bridging Evolutionary Search and Structured Research for Automated Algorithm Discovery** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.13869), [code](https://github.com/qiliuchn/OR-Agent)

3. **ConstraintBench: Benchmarking LLM Constraint Reasoning on Direct Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.22465)

4. **Algorithmic Prompt-Augmentation for Efficient LLM-Based Heuristic Design for A* Search** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.19622), [code](https://github.com/tb-git-tud/a-ceoh-evolution-of-heuristics)

5. **Text2Zinc: A Cross-Domain Dataset for Modeling Optimization and Satisfaction Problems in MiniZinc** Arxiv, 2025. [paper](https://arxiv.org/pdf/2503.10642), [code](https://huggingface.co/datasets/skadio/text2zinc)

6. **StepORLM: A Self-Evolving Framework With Generative Process Supervision For Operations Research Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.22558)

7. **Solver-Informed RL: Grounding Large Language Models for Authentic Optimization Modeling** NeurIPS, 2025. [paper](https://arxiv.org/pdf/2505.11792), [code](https://github.com/Cardinal-Operations/SIRL)

8. **ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution** ICLR, 2025. [paper](https://arxiv.org/pdf/2509.19349), [code](https://github.com/SakanaAI/ShinkaEvolve)

9. **ORMind: A Cognitive-Inspired End-to-End Reasoning Framework for Operations Research** ACL, 2025. [paper](https://arxiv.org/pdf/2506.01326), [code](https://github.com/XiaoAI1989/ORMind)

10. **OptiTree: Hierarchical Thoughts Generation with Tree Search for LLM Optimization Modeling** NeurIPS, 2025. [paper](https://arxiv.org/pdf/2510.22192), [code](https://github.com/MIRALab-USTC/OptiTree)

11. **OptiMind: Teaching LLMs to Think Like Optimization Experts** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.22979)

12. **OptimAI: Optimization from Natural Language Using LLM-Powered AI Agents** Arxiv, 2025. [paper](https://arxiv.org/pdf/2504.16918)

13. **OpenEvolve: an open-source evolutionary coding agent** GitHub, 2025. [paper](https://huggingface.co/blog/codelion/openevolve), [code](https://github.com/algorithmicsuperintelligence/openevolve)

14. **Online Algorithm Configuration for MILP Re-Optimization with LLM Guidance** Under Review, 2025. [paper](https://openreview.net/pdf?id=xbyebbS1ZF)

15. **LLM-QUBO: An End-to-End Framework for Automated QUBO Transformation from Natural Language Problem Descriptions** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.00099)

16. **Leveraging Large Language Models to Develop Heuristics for Emerging Optimization Problems** Arxiv, 2025. [paper](https://arxiv.org/pdf/2503.03350), [code](https://github.com/nico-koltermann/contextual-evolution-of-heuristics)

17. **Large Language Models and Operations Research: A Structured Survey** Arxiv, 2025. [paper](https://arxiv.org/pdf/2509.18180)

18. **Large Language Model-driven Large Neighborhood Search for Large-Scale MILP Problems** ICML, 2025. [paper](https://openreview.net/pdf?id=teUg2pMrF0), [code](https://github.com/thuiar/LLM-LNS)

19. **Large Language Model Guided Dynamic Branching Rule Scheduling in Branch-and-Bound** Under Review, 2025. [paper](https://openreview.net/pdf?id=8LCdjf7uIk)

20. **Graph Foundation Models: Bridging Language Model Paradigms and Graph Optimization** Arxiv, 2025. [paper](https://arxiv.org/abs/2509.24256)

21. **FORGE: Foundational Optimization Representations from Graph Embeddings** Arxiv, 2025. [paper](https://arxiv.org/pdf/2508.20330)

22. **EvoCut: Strengthening Integer Programs via Evolution-Guided Language Models** Arxiv, 2025. [paper](https://arxiv.org/pdf/2508.11850), [code](https://github.com/milad1378yz/EvoCut)

23. **EquivaMap: Leveraging LLMs for Automatic Equivalence Checking of Optimization Formulations** Arxiv, 2025. [paper](https://arxiv.org/pdf/2502.14760), [code](https://github.com/HumainLab/EquivaMap)

24. **DHEvo: Data-Algorithm Based Heuristic Evolution for Generalizable MILP Solving** Arxiv, 2025. [paper](https://arxiv.org/pdf/2507.15615)

25. **CodeEvolve: an open source evolutionary coding agent for algorithm discovery and optimization** Arxiv, 2025. [paper](https://arxiv.org/pdf/2510.14150), [code](https://github.com/inter-co/science-codeevolve)

26. **CO-Bench: Benchmarking Language Model Agents in Algorithm Search for Combinatorial Optimization** AAAI, 2025. [paper](https://arxiv.org/pdf/2504.04310)

27. **Automatic MILP Model Construction for Multi-Robot Task Allocation and Scheduling Based on Large Language Models** IROS, 2025. [paper](https://arxiv.org/pdf/2503.13813)

28. **AlphaEvolve: A coding agent for scientific and algorithmic discovery** Arxiv, 2025. [paper](https://arxiv.org/pdf/2506.13131), [code](https://colab.research.google.com/github/google-deepmind/alphaevolve_results/blob/master/mathematical_results.ipynb)

29. **ALE-Bench: A Benchmark for Long-Horizon Objective-Driven Algorithm Engineering** NeurIPS 2025 Datasets and Benchmarks Track, 2025. [paper](https://arxiv.org/pdf/2506.09050), [code](https://github.com/SakanaAI/ALE-Bench)

30. **Towards Foundation Models for Mixed Integer Linear Programming** ICLR, 2024. [paper](https://arxiv.org/pdf/2410.08288)

31. **Solving General Natural-Language-Description Optimization Problems with Large Language Models** NAACL, 2024. [paper](https://arxiv.org/pdf/2407.07924), [code](https://opt.alibabacloud.com/chat)

32. **Scalable Primal Heuristics Using Graph Neural Networks for Combinatorial Optimization** JAIR, 2024. [paper](https://www.jair.org/index.php/jair/article/view/14972), [code](https://github.com/furkancanturk/gnn4co)
    *Furkan Canturk, Taha Varol, Reyhan Aydogan, Okan O Ozener*

33. **ORLM: Training Large Language Models for Optimization Modeling** Operations Research, 2024. [paper](https://arxiv.org/pdf/2405.17743), [code](https://github.com/Cardinal-Operations/ORLM)

34. **OptiBench: Benchmarking Large Language Models in Optimization Modeling with Equivalence-Detection Evaluation** Under Review, 2024. [paper](https://openreview.net/forum?id=KD9F5Ap878)

35. **OptiBench Meets ReSocratic: Measure and Improve LLMs for Optimization Modeling** ICLR, 2024. [paper](https://openreview.net/forum?id=fsDZwS49uY)

36. **Multi-task Representation Learning for Mixed Integer Linear Programming** Arxiv, 2024. [paper](https://arxiv.org/pdf/2412.14409), [code](https://github.com/caidog1129/MILP_multitask)

37. **LLMOPT: Learning to Define and Solve General Optimization Problems from Scratch** ICLR, 2024. [paper](https://arxiv.org/pdf/2410.13213)

38. **LLM4Solver: Large Language Model for Efficient Algorithm Design of Combinatorial Optimization Solver** Under Review, 2024. [paper](https://openreview.net/forum?id=XTxdDEFR6D)

39. **Large Language Models for Combinatorial Optimization of Design Structure Matrix** Arxiv, 2024. [paper](https://arxiv.org/pdf/2411.12571)

40. **From Large Language Models and Optimization to Decision Optimization CoPilot: A Research Manifesto** Arxiv, 2024. [paper](https://arxiv.org/pdf/2402.16269)

41. **Evo-Step: Evolutionary Generation and Stepwise Validation for Optimizing LLMs in OR** Under Review, 2024. [paper](https://openreview.net/forum?id=aapUBU9U0D)

42. **Evaluating LLM Reasoning in the Operations Research Domain with ORQA** AAAI, 2024. [paper](https://arxiv.org/pdf/2412.17874), [code](https://github.com/nl4opt/ORQA)

43. **Diagnosing Infeasible Optimization Problems Using Large Language Models** INFOR, 2024. [paper](https://arxiv.org/pdf/2308.12923)

44. **Searching Large Neighborhoods for Integer Linear Programs with Contrastive Learning** ICML, 2023. [paper](https://proceedings.mlr.press/v202/huang23g.html), [code](https://github.com/facebookresearch/CL-LNS)
    *Taoan Huang, Aaron M Ferber, Yuandong Tian, Bistra Dilkina, Benoit Steiner*

45. **OptiMUS: Scalable Optimization Modeling with (MI)LP Solvers and Large Language Models** ICML, 2023. [paper](https://arxiv.org/pdf/2402.10172), [code](https://github.com/teshnizi/OptiMUS)

46. **On Representing Mixed-Integer Linear Programs by Graph Neural Networks** ICLR, 2023. [paper](https://openreview.net/forum?id=4gc3MGZra1d), [code](https://github.com/liujl11git/GNN-MILP)
    *Ziang Chen, Jialin Liu, Xinshang Wang, Wotao Yin*

47. **Learning to Dive in Branch and Bound** NeurIPS, 2023. [paper](https://openreview.net/forum?id=iPTF2hON1C)
    *Max B Paulus, Andreas Krause*

48. **Learning to Configure Separators in Branch-and-Cut** NeurIPS, 2023. [paper](https://openreview.net/forum?id=gf5xJVQS5p)
    *Sirui Li, Wenbin Ouyang, Max B Paulus, Cathy Wu*

49. **Learning Cut Selection for Mixed-Integer Linear Programming via Hierarchical Sequence Model** ICLR, 2023. [paper](https://openreview.net/forum?id=Zob4P9bRNcK), [code](https://github.com/MIRALab-USTC/L2O-HEM-Torch)
    *Zhihai Wang, Xijun Li, Jie Wang, Yufei Kuang, Mingxuan Yuan, Jia Zeng, Yongdong Zhang, Feng Wu*

50. **GNN-GBDT-Guided Fast Optimizing Framework for Large-scale Integer Programming** ICML, 2023. [paper](https://proceedings.mlr.press/v202/ye23e.html), [code](https://github.com/thuiar/GNN-GBDT-Guided-Fast-Optimizing-Framework)
    *Huigen Ye, Hua Xu, Hongyan Wang, Chengming Wang, Yu Jiang*

51. **GNN&GBDT-Guided Fast Optimizing Framework for Large-scale Integer Programming** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/24107)
    *Huigen, Hua-Hui Xu, Hongyan Wang, Cheng . Wang Ye, YueYen Jiang.*

52. **Chain-of-Experts: When LLMs Meet Complex Operations Research Problems** ICLR, 2023. [paper](https://openreview.net/pdf?id=HobyL1B9CZ), [code](https://github.com/xzymustbexzy/Chain-of-Experts)

53. **A GNN-Guided Predict-and-Search Framework for Mixed-Integer Linear Programming** ICLR, 2023. [paper](https://openreview.net/forum?id=pHMpgT5xWaE), [code](https://github.com/sribdcn/Predict-and-Search_MILP_method)
    *Qingyu Han, Linxin Yang, Qian Chen, Xiang Zhou, Dong Zhang, Akang Wang, Ruoyu Sun, Xiaodong Luo*

54. **A Deep Instance Generative Framework for MILP Solvers Under Limited Data Availability** NeurIPS, 2023. [paper](https://openreview.net/forum?id=AiEipk1X0c), [code](https://miralab-ustc.github.io/L2O-G2MILP)
    *Zijie Geng, Xijun Li, Jie Wang, Xiao Li, Yongdong Zhang, Feng Wu*

55. **Structural Analysis of Branch-and-Cut and the Learnability of Gomory Mixed Integer Cuts** NeurIPS, 2022. [paper](https://openreview.net/forum?id=e2gRdexoTZf)
    *Maria-Florina Balcan, Siddharth Prasad, Tuomas Sandholm, Ellen Vitercik*

56. **Ranking Constraint Relaxations for Mixed Integer Programs Using a Machine Learning Approach** Arxiv, 2022. [paper](https://arxiv.org/abs/2207.00219)
    *Jake Weiner, Xiaodong Li Andreas T. Ernst, Yuan Sun.*

57. **Lookback for Learning to Branch** Arxiv, 2022. [paper](https://arxiv.org/abs/2206.14987)
    *Prateek, Elias Boutros Khalil, Didier Chet'elat, Maxime Gasse, Yoshua Bengio, Andrea Lodi Gupta, M. Pawan Kumar.*

58. **Learning to Use Local Cuts** Arxiv, 2022. [paper](https://arxiv.org/abs/2206.11618)
    *Timo Berthold, Matteo Francobaldi, Gregor Hendel*

59. **Learning to Search in Local Branching** AAAI, 2022. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/20294), [code](https://github.com/pandat8/ML4LB)
    *Defeng Liu, Matteo Fischetti, Andrea Lodi*

60. **Learning to Cut by Looking Ahead: Cutting Plane Selection via Imitation Learning** ICML, 2022. [paper](https://proceedings.mlr.press/v162/paulus22a.html)
    *Max B., Giulia Zarpellon, Andreas Krause, Laurent Charlin Paulus, Chris J. Maddison.*

61. **Learning to Branch with Tree-aware Branching Transformers** Knowledge-Based Systems, 2022. [paper](https://www.sciencedirect.com/science/article/pii/S0950705122007298?via%3Dihub), [code](https://github.com/linjc16/TBranT)
    *Jiacheng Lin, Jialin Zhu, Huangang Wang, Tao Zhang*

62. **Learning to Branch with Tree MDPs** Arxiv, 2022. [paper](https://arxiv.org/abs/2205.11107), [code](https://github.com/lascavana/rl2branch)
    *Lara, F. Chen, Didier Ch'etelat, Maxime Gasse, Andrea Lodi, N. Yorke-Smith Scavuzzo, Karen Aardal.*

63. **Learning to Accelerate Approximate Methods for Solving Integer Programming via Early Fixing** Arxiv, 2022. [paper](https://arxiv.org/abs/2207.02087), [code](https://github.com/SCLBD/Accelerated-Lpbox-ADMM)
    *Longkang Li, Baoyuan Wu.*

64. **DOGE-Train: Discrete Optimization on GPU with End-to-end Training** Arxiv, 2022. [paper](https://arxiv.org/abs/2205.11638)
    *Ahmed Abbas, Paul Swoboda*

65. **Deep Reinforcement Learning for Exact Combinatorial Optimization: Learning to Branch** Arxiv, 2022. [paper](https://arxiv.org/abs/2206.06965)
    *Tianyu Zhang, Amin Banitalebi-Dehkordi, Yong Zhang*

66. **Constrained Discrete Black-Box Optimization using Mixed-Integer Programming** ICML, 2022. [paper](https://proceedings.mlr.press/v162/papalexopoulos22a.html)
    *Theodore, Christian Tjandraatmadja, Ross Anderson, Juan Pablo Vielma Papalexopoulos, Daving Belanger.*

67. **An Improved Reinforcement Learning Algorithm for Learning to Branch** Arxiv, 2022. [paper](https://arxiv.org/abs/2201.06213)
    *Qingyu Qu, Xijun Li, Yunfan Zhou, Jia Zeng, Mingxuan Yuan, Jie Wang, Jinhu Lv, Kexin Liu, Kun Mao*

68. **A Deep Reinforcement Learning Framework For Column Generation** Arxiv, 2022. [paper](https://arxiv.org/abs/2206.02568)
    *Cheng, Amine Mohamed Aboussalah, Elias Boutros Khalil, Juyoung Wang Chi, Zoha Sherkat-Masoumi.*

69. **Reinforcement Learning for (Mixed) Integer Programming: Smart Feasibility Pump** ICML Workshop, 2021. [paper](https://arxiv.org/abs/2102.09663)
    *Meng Qi, Mengxin Wang, Zuo-Jun Shen*

70. **Parameterizing Branch-and-Bound Search Trees to Learn Branching Policies** AAAI, 2021. [paper](https://www.aaai.org/AAAI21Papers/AAAI-9826.ZarpellonG.pdf), [code](https://github.com/ds4dm/branch-search-trees)
    *Giulia Zarpellon, Jason Jo, Andrea Lodi, Yoshua Bengio*

71. **Offline Constraint Screening for Online Mixed-integer Optimization** Arxiv, 2021. [paper](https://arxiv.org/abs/2103.13074)
    *Asunción Jiménez-Cordero, Juan Miguel Morales, Salvador Pineda*

72. **Mixed Integer Programming versus Evolutionary Computation for Optimizing a Hard Real-World Staff Assignment Problem** ICAPS, 2021. [paper](https://ojs.aaai.org/index.php/ICAPS/article/view/3521)
    *Jannik Peters, Daniel Stephan, Isabel Amon, Hans Gawendowicz, Julius Lischeid, Lennart Salabarria, Jonas Umland, Felix Werner, Martin S Krejca, Ralf Rothenberger, others*

73. **Learning to Solve Large-scale Security-constrained Unit Commitment Problems** INFORMS Journal on Computing, 2021. [paper](https://pubsonline.informs.org/doi/abs/10.1287/ijoc.2020.0976)
    *{\'A}linson S Xavier, Feng Qiu, Shabbir Ahmed*

74. **Learning to Select Cuts for Efficient Mixed-Integer Programming** Arxiv, 2021. [paper](https://arxiv.org/abs/2105.13645)
    *Zeren Huang, Kerong Wang, Furui Liu, Hui-ling Zhen, Weinan Zhang, Mingxuan Yuan, Jianye Hao, Yong Yu, Jun Wang*

75. **Learning To Scale Mixed-Integer Programs** AAAI, 2021. [paper](https://www.aaai.org/AAAI21Papers/AAAI-7940.BertholdT.pdf)
    *Timo Berthold, Gregor Hendel*

76. **Learning Pseudo-Backdoors for Mixed Integer Programs** AAAI, 2021. [paper](https://arxiv.org/pdf/2106.05080.pdf)
    *Aaron Ferber, Jialin Song, Bistra Dilkina, Yisong Yue*

77. **Learning Primal Heuristics for Mixed Integer Programs** IJCNN, 2021. [paper](https://arxiv.org/pdf/2107.00866.pdf)
    *Yunzhuang Shen, Yuan Sun, Andrew Eberhard, Xiaodong Li*

78. **Learning large neighborhood search policy for integer programming** NeurlPS, 2021. [paper](https://proceedings.neurips.cc/paper/2021/hash/fc9e62695def29ccdb9eb3fed5b4c8c8-Abstract.html)
    *Yaoxin Wu, Wen Song, Zhiguang Cao, Jie Zhang*

79. **Generative Deep Learning for Decision Making in Gas Networks** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.02125)
    *Lovis Anderson, Mark Turner, Thorsten Koch*

80. **Confidence Threshold Neural Diving** NeurIPS ML4CO Competition Workshop, 2021. [paper](https://arxiv.org/abs/2202.07506)
    *Taehyun Yoon*

81. **CombOptNet: Fit the Right NP-Hard Problem by Learning Integer Programming Constraints** Arxiv, 2021. [paper](https://arxiv.org/abs/2105.02343), [code](https://github.com/martius-lab/CombOptNet)
    *Anselm Paulus, Michal Rolinek, Vit Musil, Brandon Amos, Georg Martius*

82. **Solving Mixed Integer Programs Using Neural Networks** Arxiv, 2020. [paper](https://arxiv.org/abs/2012.13349)
    *Vinod Nair, Sergey Bartunov, Felix Gimeno, Ingrid von Glehn, Pawel Lichocki, Ivan Lobov, Brendan O'Donoghue, Nicolas Sonnerat, Christian Tjandraatmadja, Pengming Wang, others*

83. **Reinforcement learning for variable selection in a branch and bound algorithm** International Conference on Integration of Constraint Programming, 2020. [paper](https://link.springer.com/chapter/10.1007/978-3-030-58942-4_12)
    *Marc Etheve, Zacharie Al{\`e}s, C{\^o}me Bissuel, Olivier Juan, Safia Kedad-Sidhoum*

84. **Reinforcement Learning for Integer Programming: Learning to Cut** ICML, 2020. [paper](http://proceedings.mlr.press/v119/tang20a.html)
    *Yunhao Tang, Shipra Agrawal, Yuri Faenza*

85. **Random sampling and machine learning to understand good decompositions** Annals of Operations Research, 2020. [paper](https://link.springer.com/article/10.1007/s10479-018-3067-9)
    *Saverio Basso, Alberto Ceselli, Andrea Tettamanzi*

86. **Neural Large Neighborhood Search** NeurlPS Workshop, 2020. [paper](https://openreview.net/forum?id=xEQhKANoVW)
    *Vinod Nair, Mohammad Alizadeh, others*

87. **Learning Efficient Search Approximation in Mixed Integer Branch and Bound** Arxiv, 2020. [paper](https://arxiv.org/abs/2007.03948)
    *Kaan Yilmaz, Neil Yorke-Smith*

88. **Learning a Large Neighborhood Search Algorithm for Mixed Integer Programs** Arxiv, 2020. [paper](https://arxiv.org/abs/2107.10201)
    *Nicolas Sonnerat, Pengming Wang, Ira Ktena, Sergey Bartunov, Vinod Nair*

89. **Improving Learning to Branch via Reinforcement Learning** NeurIPS Workshop, 2020. [paper](https://openreview.net/forum?id=z4D7-PTxTb)
    *Haoran Sun, Wenbo Chen, Hui Li, Le Song*

90. **Hybrid Models for Learning to Branch** NeurlPS, 2020. [paper](https://arxiv.org/abs/2006.15212), [code](https://github.com/pg2455/Hybrid-learn2branch)
    *Prateek Gupta, Maxime Gasse, Elias B Khalil, M Pawan Kumar, Andrea Lodi, Yoshua Bengio*

91. **Accelerating Primal Solution Findings for Mixed Integer Programs Based on Solution Prediction** AAAI, 2020. [paper](https://arxiv.org/abs/1906.09575)
    *Jian-Ya, Chao Zhang, Lei Shen, Shengyin Li, Bing Wang, Yinghui Xu Ding, Le Song*

92. **A General Large Neighborhood Search Framework for Solving Integer Linear Programs** NeurlPS, 2020. [paper](https://arxiv.org/abs/2004.00422)
    *Jialin Song, Ravi Lanka, Yisong Yue, Bistra Dilkina*

93. **Exact Combinatorial Optimization with Graph Convolutional Neural Networks** NeurlPS, 2019. [paper](https://arxiv.org/abs/1906.01629), [code](https://github.com/ds4dm/learn2branch)
    *Maxime Gasse, Didier Chetelat, Nicola Ferroni, Laurent Charlin, Andrea Lodi*

94. **Learning When to Use a Decomposition** International conference on AI and OR techniques in constraint programming for combinatorial optimization problems, 2017. [paper](https://link.springer.com/chapter/10.1007/978-3-319-59776-8_16)
    *Markus Kruber, L{\u}bbecke Marco E, Parmentier Axel*

95. **Learning to Run Heuristics in Tree Search** IJCAI, 2017. [paper](https://www.ijcai.org/proceedings/2017/0092.pdf)
    *Elias B Khalil, Bistra Dilkina, George L Nemhauser, Shabbir Ahmed, Yufen Shao*

96. **Learningto Branch in Mixed Integer Programming** AAAI, 2016. [paper](https://www.aaai.org/ocs/index.php/AAAI/AAAI16/paper/download/12514/11657)
    *E. B. Khalil, P. L. Bodic, L. Song, G. Nemhauser, B. Dilkina*

97. **Dash: Dynamic Approach for Switching Heuristics** European Journal of Operational Research, 2016. [paper](https://www.sciencedirect.com/science/article/pii/S0377221715007559)
    *Giovanni Di Liberto, Serdar Kadioglu, Kevin Leo, Yuri Malitsky*

98. **Learning to Search in Branch-and-Bound Algorithms** NeurlPS, 2014. [paper](http://papers.nips.cc/paper/5495-learning-to-search-in-branch-and-bound-algorithms)
    *He He, Hal Daume III, Jason M Eisner*

99. **A Aupervised Machine Learning Approach to Variable Branching in Branch-and-bound** Citeseer, 2014. [paper](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=f35ba2bbc87dd31ae0a89d3ed9538fec9d15b4f0)
    *Alejandro Marcos Alvarez, Quentin Louveaux, Louis Wehenkel*

100. **Non-model-based Search Guidance for Set Partitioning Problems** AAAI, 2012. [paper](https://www.aaai.org/ocs/index.php/AAAI/AAAI12/paper/view/5082)
    *Serdar Kadioglu, Yuri Malitsky, Meinolf Sellmann*

101. **Sequential model-based optimization for general algorithm configuration** International conference on learning and intelligent optimization, 2011. [paper](https://link.springer.com/chapter/10.1007/978-3-642-25566-3_40)
    *Frank Hutter, Holger H Hoos, Kevin Leyton-Brown*

### [Causal Discovery](#content) · *9 papers*

1. **Sample Complexity Bounds for Score-Matching: Causal Discovery and Generative Modeling** NeurIPS, 2023. [paper](https://openreview.net/forum?id=uNnPWR66b8)
    *Zhenyu Zhu, Francesco Locatello, Volkan Cevher*

2. **Nonlinear Causal Discovery with Latent Confounders** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/23789), [code](https://github.com/chunlinli/defuse)
    *David Kaltenpoth, Jilles Vreeken*

3. **Diffusion Models for Causal Discovery via Topological Ordering** ICLR, 2023. [paper](https://openreview.net/forum?id=Idusfje4-Wq), [code](https://github.com/vios-s/DiffAN)
    *Pedro Sanchez, Xiao Liu, Alison Q O'Neil, Sotirios A Tsaftaris*

4. **CUTS: Neural Causal Discovery from Irregular Time-Series Data** ICLR, 2023. [paper](https://openreview.net/forum?id=UG8bQcD3Emv), [code](https://github.com/jarrycyx/unn)
    *Yuxiao Cheng, Runzhao Yang, Tingxiong Xiao, Zongren Li, Jinli Suo, Kunlun He, Qionghai Dai*

5. **Boosting Causal Discovery via Adaptive Sample Reweighting** ICLR, 2023. [paper](https://openreview.net/forum?id=LNpMtk15AS4), [code](https://github.com/anzhang314/ReScore)
    *An Zhang, Fangfu Liu, Wenchang Ma, Zhibo Cai, Xiang Wang, Tat-seng Chua*

6. **BayesDAG: Gradient-Based Posterior Inference for Causal Discovery** NeurIPS, 2023. [paper](https://openreview.net/forum?id=woptnU6fh1)
    *Yashas Annadani, Nick Pawlowski, Joel Jennings, Stefan Bauer, Cheng Zhang, Wenbo Gong*

7. **Large-Scale Differentiable Causal Discovery of Factor Graphs** NeurIPS, 2022. [paper](https://openreview.net/forum?id=k713e8vXzwR), [code](https://github.com/Genentech/dcdfg)
    *Romain Lopez, Jan-Christian H{\"u}tter, Jonathan K Pritchard, Aviv Regev*

8. **Causal Discovery with Reinforcement Learning.** ICLR, 2020. [paper](https://arxiv.org/abs/1906.04477)
    *Shengyu Zhu, Ignavier Ng, Zhitang Chen*

9. **DAGs with NO TEARS: Continuous Optimization for Structure Learning.** NeurIPS, 2018. [paper](https://arxiv.org/pdf/1803.01422.pdf)
    *Xun Zheng, Bryon Aragam, Pradeep Ravikumar, Eric Xing*

### [Game Theoretic Semantics](#content) · *1 papers*

1. **First-Order Problem Solving through Neural MCTS based Reinforcement Learning.** Arxiv, 2021. [paper](https://arxiv.org/abs/2101.04167)
    *Ruiyang Xu, Prashank Kadam, Karl Lieberherr*

### [Differentiable Optimization](#content) · *6 papers*

1. **SurCo: Learning Linear Surrogates For Combinatorial Nonlinear Optimization Problems** ICML, 2023. [paper](https://arxiv.org/abs/2210.12547), [code](https://github.com/facebookresearch/SurCo)
    *Aaron M Ferber, Taoan Huang, Daochen Zha, Martin Schubert, Benoit Steiner, Bistra Dilkina, Yuandong Tian*

2. **Backpropagation through Combinatorial Algorithms: Identity with Projection Works** ICLR, 2023. [paper](https://openreview.net/forum?id=JZMR727O29), [code](https://github.com/martius-lab/solver-differentiation-identity)
    *Subham Sekhar Sahoo, Anselm Paulus, Marin Vlastelica, Vít Musil, Volodymyr Kuleshov, Georg Martius*

3. **MIPaaL: Mixed Integer Program as a Layer** AAAI, 2020. [paper](https://ojs.aaai.org//index.php/AAAI/article/view/5509), [code](https://github.com/amf272/MIPaaL/)
    *Aaron Ferber, Bryan Wilder, Bistra Dilkina, Milind Tambe*

4. **Differentiation of Blackbox Combinatorial Solvers** ICLR, 2020. [paper](https://arxiv.org/pdf/1912.02175v2.pdf), [code](https://github.com/martius-lab/blackbox-backprop)
    *Marin Vlastelica, Anselm Paulus, Vít Musil, Georg Martius, Michal Rolínek*

5. **Differentiation of blackbox combinatorial solvers** ICLR, 2020. [paper](https://openreview.net/forum?id=BkevoJSYPB), [code](https://github.com/martius-lab/blackbox-backprop)
    *Marin Vlastelica Pogani, Anselm Paulus, Vit Musil, Georg Martius, Michal Rolinek*

6. **Differentiable Learning of Submodular Models** NeurIPS, 2017. [paper](https://papers.NeurIPS.cc/paper/2017/hash/192fc044e74dffea144f9ac5dc9f3395-Abstract.html), [code](https://github.com/josipd/torch-submod)
    *Josip Djolonga, Andreas Krause*

### [Car Dispatch](#content) · *2 papers*

1. **MAPF-GPT: Imitation Learning for Multi-Agent Pathfinding at Scale** AAAI, 2024. [paper](https://arxiv.org/pdf/2409.00134), [code](https://github.com/Cognitive-AI-Systems/MAPF-GPT)

2. **Dispatch of autonomous vehicles for taxi services: A deep reinforcement learning approach** Transportation Research, 2020. [paper](https://www.sciencedirect.com/science/article/pii/S0968090X19312227)
    *Chao Mao, Yulin Liu, Zuo-Jun (Max) Shen*

### [Electronic Design Automation](#content) · *9 papers*

1. **HeuriGym: An Agentic Benchmark for LLM-Crafted Heuristics in Combinatorial Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2506.07972), [code](https://github.com/cornell-zhang/heurigym)
    *Hongzheng Chen, Yingheng Wang, Yaohui Cai, Hins Hu, Jiajie Li, Shirley Huang, Chenhui Deng, Rongjian Liang, Shufeng Kong, Haoxing Ren, Samitha Samaranayake, Carla P. Gomes, Zhiru Zhang*

2. **AutoFloorplan: Evolving Heuristics for Chip Floorplanning with Large Language Models and Textual Gradient-Guided Repair** Under Review, 2025. [paper](https://openreview.net/pdf?id=DS2iool3nv)

3. **ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution** NeurIPS, 2024. [paper](https://arxiv.org/pdf/2402.01145), [code](https://github.com/ai4co/reevo)

4. **HubRouter: Learning Global Routing via Hub Generation and Pin-hub Connection** NeurIPS, 2023. [paper](https://openreview.net/forum?id=f0Jj3C3Pnp)
    *Xingbo Du, Chonghua Wang, Ruizhe Zhong, Junchi Yan*

5. **CktGNN: Circuit Graph Neural Network for Electronic Design Automation** ICLR, 2023. [paper](https://openreview.net/forum?id=NE2911Kq1sp)
    *Zehao Dong, Weidong Cao, Muhan Zhang, Dacheng Tao, Yixin Chen, Xuan Zhang*

6. **Unsupervised Learning for Combinatorial Optimization with Principled Objective Relaxation** NeurIPS, 2022. [paper](https://openreview.net/forum?id=HjNn9oD_v47), [code](https://github.com/Graph-COM/CO_ProxyDesign)
    *Haoyu Peter Wang, Nan Wu, Hang Yang, Cong Hao, Pan Li*

7. **The Policy-gradient Placement and Generative Routing Neural Networks for Chip Design** NeurIPS, 2022. [paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/a8b8c1ad51df1b93d9e3d1fca75debbf-Abstract-Conference.html), [code](https://github.com/Thinklab-SJTU/EDA-AI)
    *Ruoyu Cheng, Xianglong Lyu, Yang Li, Junjie Ye, Jianye Hao, Junchi Yan*

8. **On Joint Learning for Solving Placement and Routing in Chip Design** NeurIPS, 2021. [paper](https://arxiv.org/abs/2111.00234), [code](https://github.com/Thinklab-SJTU/EDA-AI)
    *Ruoyu Cheng, Junchi Yan*

9. **A graph placement methodology for fast chip design** Nature, 2021. [paper](https://www.nature.com/articles/s41586-021-03544-w.pdf)
    *Azalia Mirhoseini, Anna Goldie, Mustafa Yazgan, Joe Wenjie Jiang, Ebrahim Songhori, Shen Wang, Young-Joon Lee, Eric Johnson, Omkar Pathak, Azade Nazi, Jiwoo Pak, Andy Tong, Kavya Srinivasa, William Hang, Emre Tuncer, Quoc V. Le, James Laudon, Richard Ho, Roger Carpenter, Jeff Dean*

### [Conjunctive Query Containment](#content) · *1 papers*

1. **It's Not What Machines Can Learn It's What We Cannot Teach** ICML, 2020. [paper](http://proceedings.mlr.press/v119/yehuda20a/yehuda20a.pdf)
    *Gal Yehuda, Moshe Gabel, Assaf Schuster*

### [Virtual Network Embedding](#content) · *13 papers*

1. **GAL-VNE: Solving the VNE Problem with Global Reinforcement Learning and Local One-Shot Neural Prediction** KDD, 2023. [paper](https://dl.acm.org/doi/10.1145/3580305.3599358), [code](https://github.com/Thinklab-SJTU/GAL-VNE)
    *Haoyu Geng, Runzhong Wang, Fei Wu, Junchi Yan*

2. **Dynamic Virtual Network Embedding Algorithm Based on Graph Convolution Neural Network and Reinforcement Learning** IoT-J, 2021. [paper](https://ieeexplore.ieee.org/document/9475485)
    *Peiying Zhang, Chao Wang, Neeraj Kumar, Weishan Zhang, Lei Liu*

3. **DRL-SFCP: Adaptive Service Function Chains Placement with Deep Reinforcement Learning** ICC, 2021. [paper](https://ieeexplore.ieee.org/document/9500964)
    *Tianfu Wang, Qilin Fan, Xiuhua Li, Xu Zhang, Qingyu Xiong, Shu Fu, Min Gao*

4. **Deep Reinforcement Based Optimization of Function Splitting in Virtualized Radio Access Networks** ICC, 2021. [paper](https://ieeexplore.ieee.org/document/9473703), [code](https://github.com/rubensolozabal/vnf_placement_optimization_rl)
    *Fahri Wisnu Murti, Samad Ali, Matti Latva-aho*

5. **Automatic Virtual Network Embedding A Deep Reinforcement Learning Approach With Graph Convolutional Networks** J-SAC, 2020. [paper](https://ieeexplore.ieee.org/document/9060910)
    *Zhongxia Yan, Jingguo Ge, Yulei Wu, Liangxiong Li, Tong Li*

6. **Accelerating Virtual Network Embedding with Graph Neural Networks** CNSM, 2020. [paper](https://ieeexplore.ieee.org/document/9269128)
    *Farzad Habibi, Mahdi Dolati, Ahmad Khonsari, Majid Ghaderi*

7. **A Q-learning-based approach for virtual network embedding in data center** NCA, 2020. [paper](https://link.springer.com/article/10.1007/s00521-019-04376-6)
    *Ying Yuan, Zejie Tian, Cong Wang, Fanghui Zheng, Yanxia Lv*

8. **A Continuous-Decision Virtual Network Embedding Scheme Relying on Reinforcement Learning** IEEE TNSM, 2020. [paper](https://ieeexplore.ieee.org/document/8982091)
    *Haipeng Yao, Sihan Ma, Jingjing Wang, Peiying Zhang, Chunxiao Jiang, Song Guo*

9. **NFVdeep: Adaptive Online Service Function Chain Deployment with Deep Reinforcement Learning** IWQoS, 2019. [paper](https://ieeexplore.ieee.org/document/9068634)
    *Yikai Xiao, Qixia Zhang, Fangming Liu, Jia Wang, Miao Zhao, Zhongxing Zhang, Jiaxing Zhang*

10. **A Virtual Network Embedding Algorithm Based On Double-Layer Reinforcement Learning** TCJ, 2019. [paper](https://ieeexplore.ieee.org/document/9514735)
    *Meng Li, MeiLian Lu*

11. **NeuroViNE: A Neural Preprocessor for Your Virtual Network Embedding Algorithm** INFOCOM, 2018. [paper](https://ieeexplore.ieee.org/document/8486263)
    *Andreas Blenk, Patrick Kalmbach, Johannes Zerwas, Michael Jarschel, Stefan Schmid, Wolfgang Kellerer*

12. **A novel reinforcement learning algorithm for virtual network embedding** Neurocomputing, 2018. [paper](https://www.sciencedirect.com/science/article/abs/pii/S0925231218300420)
    *Haipeng Yao, Xu Chen, Maozhen Li, Peiying Zhang, Luyao Wang*

13. **Virtual Network Embedding via Monte Carlo Tree Search** IEEE Trans. Cybern, 2017. [paper](https://ieeexplore.ieee.org/document/7859375)
    *Soroush Haeri, Ljiljana Trajković*

### [Predict+Optimize](#content) · *16 papers*

1. **Two-Stage Predict+Optimize for Mixed Integer Linear Programs with Unknown Parameters in Constraints** NeurIPS, 2023. [paper](https://openreview.net/forum?id=0tnhFpyWjb), [code](https://github.com/elizabethxyhu/neurips_two_stage_predict-optimize)
    *Xinyi Hu, Jasper CH Lee, Jimmy HM Lee*

2. **Predict+ Optimize for packing and covering LPs with unknown parameters in constraints** AAAI, 2023. [paper](https://dl.acm.org/doi/10.1609/aaai.v37i4.25513)
    *Xinyi Hu, Jasper C.H. Lee, Jimmy H.M. Lee*

3. **End-to-End Stochastic Optimization with Energy-Based Model** NeurIPS, 2022. [paper](https://openreview.net/forum?id=_sYOodxTMcF), [code](https://github.com/Lingkai-Kong/so-ebm)
    *Lingkai Kong, Jiaming Cui, Yuchen Zhuang, Rui Feng, B. Aditya Prakash, Chao Zhang*

4. **Deep Declarative Networks** TPAMI, 2022. [paper](https://ieeexplore.ieee.org/document/9355027), [code](https://github.com/anucvml/ddn)
    *Stephen Gould, Richard Hartley, Dylan Campbell*

5. **An Exact Symbolic Reduction of Linear Smart Predict+Optimize to Mixed Integer Linear Programming** ICML, 2022. [paper](https://proceedings.mlr.press/v162/jeong22a.html), [code](https://github.com/jihwan-jeong/xaddpy)
    *Jihwan Jeong, Parth Jaggi, Andrew Butler, Scott Sanner*

6. **Implicit MLE: Backpropagating Through Discrete Exponential Family Distributions** NeurIPS, 2021. [paper](https://openreview.net/forum?id=lR4aaWCQgB), [code](https://github.com/uclnlp/torch-imle)
    *Mathias Niepert, Pasquale Minervini, Luca Franceschi*

7. **COPS: Combinatorial Optimization for Panoptic Segmentation: A Fully Differentiable Approach** NeurIPS, 2021. [paper](https://proceedings.neurips.cc/paper/2021/hash/83a368f54768f506b833130584455df4-Abstract.html), [code](https://github.com/aabbas90/COPS)
    *Ahmed Abbas, Paul Swoboda*

8. **Contrastive Losses and Solution Caching for Predict-and-Optimize** IJCAI, 2021. [paper](https://www.ijcai.org/proceedings/2021/0390.pdf), [code](https://github.com/jayman91/ltr-predopt)
    *Maxime Mulamba, Jayanta Mandi, Michelangelo Diligenti, Michele Lombardi, Victor Bucarey, Tias Guns*

9. **A Surrogate Objective Framework for Prediction+Programming with Soft Constraints** NeurIPS, 2021. [paper](https://openreview.net/forum?id=9Sa2xh4mGR), [code](https://github.com/PredOptwithSoftConstraint/PredOptwithSoftConstraint)
    *Kai Yan, Jie Yan, Chuan Luo, Liting Chen, Qingwei Lin, Dongmei Zhang*

10. **Smart Predict-and-Optimize for Hard Combinatorial Optimization Problems** AAAI, 2020. [paper](https://arxiv.org/abs/1911.10092), [code](https://github.com/JayMan91/aaai_predit_then_optimize)
    *Jayanta Mandi, Emir Demirovic, Peter J. Stuckey, Tias Guns*

11. **Interior Point Solving for LP-based prediction+optimization** NeurIPS, 2020. [paper](https://proceedings.neurips.cc//paper/2020/hash/51311013e51adebc3c34d2cc591fefee-Abstract.html), [code](https://github.com/JayMan91/NeurIPSIntopt)
    *Jayanta Mandi, Tias Guns*

12. **Automatically Learning Compact Quality-aware Surrogates for Optimization Problems** NeurIPS, 2020. [paper](https://openreview.net/forum?id=v8hzdOdOle)
    *Kai Wang, Bryan Wilder, Andrew Perrault, Milind Tambe*

13. **Predict+optimise with ranking objectives: exhaustively learning linear functions** IJCAI, 2019. [paper](https://dl.acm.org/doi/abs/10.5555/3367032.3367186)
    *Emir Demirovic, Peter J. Stuckey, James Bailey, Jeffrey Chan, Christopher Leckie, Kotagiri Ramamohanarao, Tias Guns*

14. **Melding the Data-Decisions Pipeline: Decision-Focused Learning for Combinatorial Optimization** AAAI, 2019. [paper](https://ojs.aaai.org//index.php/AAAI/article/view/3982)
    *Bryan Wilder, Bistra Dilkina, Milind Tambe*

15. **Differentiable Convex Optimization Layers** NeurIPS, 2019. [paper](https://dl.acm.org/doi/abs/10.5555/3454287.3455145), [code](https://github.com/cvxgrp/cvxpylayers)
    *Akshay Agrawal, Stephen Boyd*

16. **OptNet: differentiable optimization as a layer in neural networks** ICML, 2017. [paper](https://dl.acm.org/doi/abs/10.5555/3305381.3305396), [code](https://github.com/locuslab/optnet)
    *Brandon Amos, J. Zico Kolter*

### [Optimal Power Flow](#content) · *4 papers*

1. **Ensuring DNN Solution Feasibility for Optimization Problems with Linear Constraints** ICLR, 2023. [paper](https://openreview.net/forum?id=QVcDQJdFTG)
    *Tianyu Zhao, Xiang Pan, Minghua Chen, Steven Low*

2. **Adversarially Robust Learning for Security-Constrained Optimal Power Flow** NeurIPS, 2021. [paper](https://proceedings.neurips.cc/paper/2021/hash/f0f07e680de407b0f12abf15bd520097-Abstract.html)
    *Priya Donti, Aayushya Agarwal, Neeraj Vijay Bedmutha, Larry Pileggi, J. Zico Kolter*

3. **Predicting AC Optimal Power Flows: Combining Deep Learning and Lagrangian Dual Methods** AAAI, 2020. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/5403), [code](https://github.com/AIPOpt-Lab-SU/lagrangian-dual-deep-learning)
    *Ferdinando Fioretto, Terrence W.K. Mak, Pascal Van Hentenryck*

4. **DeepOPF: A Deep Neural Network Approach for Security-Constrained DC Optimal Power Flow** SmartGridComm, 2019. [paper](https://ieeexplore.ieee.org/document/8909795)
    *Xiang Pan, Tianyu Zhao, Minghua Chen*

### [Facility Location Problem](#content) · *7 papers*

1. **TPD-AHD: Textual Preference Differentiation for LLM-Based Automatic Heuristic Design** Under Review, 2025. [paper](https://openreview.net/pdf?id=VEMknlIPtM)

2. **A Comprehensive Evaluation of Contemporary ML-Based Solvers for Combinatorial Optimization** ICML 2025 Workshop AI4Math, 2025. [paper](https://arxiv.org/pdf/2505.16952), [code](https://huggingface.co/datasets/CO-Bench/FrontierCO)

3. **GOAL: A Generalist Combinatorial Optimization Agent Learner** ICLR, 2024. [paper](https://arxiv.org/pdf/2406.15079), [code](https://github.com/naver/goal-co)

4. **Towards One-shot Neural Combinatorial Solvers: Theoretical and Empirical Notes on the Cardinality-Constrained Case** ICLR, 2023. [paper](https://openreview.net/forum?id=h21yJhdzbwz), [code](https://github.com/Thinklab-SJTU/One-Shot-Cardinality-NN-Solver)
    *Runzhong Wang, Li Shen, Yiting Chen, Junchi Yan, Xiaokang Yang, Dacheng Tao*

5. **Solving uncapacitated P-Median problem with reinforcement learning assisted by graph attention networks** Applied Intelligence, 2023. [paper](https://link.springer.com/article/10.1007/s10489-022-03453-z)
    *Chenguang Wang, Congying Han, Tiande Guo, Man Ding*

6. **Large Language Models for Supply Chain Optimization** Arxiv, 2023. [paper](https://arxiv.org/pdf/2307.03875), [code](https://github.com/microsoft/OptiGuide)

7. **Learning to Prune Instances of k-median and Related Problems.** ALENEX, 2022. [paper](https://dx.doi.org/10.1137/1.9781611977042.15), [code](https://github.com/dajwani/alenex22)
    *Dena Tayebi, Saurabh Ray, Deepak Ajwani*

### [Combinatorial Drug Recommendation](#content) · *7 papers*

1. **MoleRec: Combinatorial Drug Recommendation with Substructure-Aware Molecular Representation Learning** WWW, 2023. [paper](https://dl.acm.org/doi/10.1145/3543507.3583872), [code](https://github.com/yangnianzu0515/MoleRec)
    *Nianzu Yang, Kaipeng Zeng, Qitian Wu, Junchi Yan*

2. **Learning Subpocket Prototypes for Generalizable Structure-based Drug Design** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25062)
    *Zaixin Zhang, Qi Liu*

3. **Enhancing Activity Prediction Models in Drug Discovery with the Ability to Understand Human Language** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/24953)
    *Philipp Seidl, Andreu Vall, Sepp Hochreiter, Gunter Klambauer*

4. **DECOMPDIFF: Diffusion Models with Decomposed Priors for Structure-Based Drug Design** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/23697)
    *Jiaqi Guan, Xiangxin Zhou, Yuwei Yang, Yu Bao, Jian-wei Peng, Jianzhu Ma, Q. Liu, Liang Wang, Quanquan Gu*

5. **Debiased, Longitudinal and Coordinated Drug Recommendation through Multi-Visit Clinic Recordss** NeurIPS, 2022. [paper](https://openreview.net/forum?id=zVglD2W0EAS), [code](https://github.com/ssshddd/DrugRec)
    *Hongda Sun, Shufang Xie, Shuqi Li, Yuhan Chen, Ji-Rong Wen, Rui Yan*

6. **SafeDrug: Dual Molecular Graph Encoders for Recommending Effective and Safe Drug Combinations** IJCAI, 2021. [paper](https://www.ijcai.org/proceedings/2021/0514.pdf), [code](https://github.com/ycq091044/SafeDrug)
    *Chaoqi Yang, Cao Xiao, Fenglong Ma, Lucas Glass, Jimeng Sun*

7. **GAMENet: Graph Augmented MEmory Networks for Recommending Medication Combination** AAAI, 2019. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/3905), [code](https://github.com/sjy1203/GAMENet)
    *Junyuan Shang, Cao Xiao, Tengfei Ma, Hongyan Li, Jimeng Sun*

### [Stochastic Combinatorial Optimization](#content) · *8 papers*

1. **LLaMEA-SAGE: Guiding Automated Algorithm Design with Structural Feedback from Explainable AI** Arxiv, 2026. [paper](https://arxiv.org/pdf/2601.21511)

2. **From Sequential to Parallel: Reformulating Dynamic Programming as GPU Kernels for Large-Scale Stochastic Combinatorial Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2602.05179), [code](https://github.com/Jingyi-poly/2-stage-IRP-GPU/tree/CVRPSD-split-GPU)
    *Jingyi Zhao, Linxin Yang, Haohua Zhang, Qile He, Tian Ding*

3. **Code Evolution Graphs: Understanding Large Language Model Driven Design of Algorithms** GECCO, 2025. [paper](https://arxiv.org/pdf/2503.16668)

4. **Learning to Optimize with Stochastic Dominance Constraints** AISTATS, 2023. [paper](https://proceedings.mlr.press/v206/dai23b.html)
    *Hanjun Dai, Yuan Xue, Niao He, Yixin Wang, Na Li, Dale Schuurmans, Bo Dai*

5. **Neur2SP- Neural Two-Stage Stochastic Programming** NeurIPS, 2022. [paper](https://openreview.net/forum?id=HQDvPsdXS-F), [code](https://github.com/khalil-research/Neur2SP)
    *Rahul Mihir Patel, Justin Dumouchelle, Elias Boutros Khalil, Merve Bodur*

6. **A New Approach for Vehicle Routing with Stochastic Demand- Combining Route Assignment with Process Flexibility** OR, 2022. [paper](https://pubsonline.informs.org/doi/abs/10.1287/opre.2022.2304)
    *Kirby Ledvina, Hanzhang Qin, David Simchi-Levi, Yehua Wei*

7. **USCO-Solver: Solving Undetermined Stochastic Combinatorial Optimization Problems** NeurIPS, 2021. [paper](https://openreview.net/forum?id=P85jauwfNCV), [code](https://github.com/cdslabamotong/USCO-Solver)
    *Guangmo Tong*

8. **Learning fast optimizers for contextual stochastic integer programs** UAI, 2018. [paper](http://auai.org/uai2018/proceedings/papers/217.pdf)
    *V Nair, D Dvijotham, I Dunning, O Vinyals*

### [Vertex Cover](#content) · *12 papers*

1. **Hard Constraints Meet Soft Generation: Guaranteed Feasibility for LLM-based Combinatorial Optimization** Arxiv, 2026. [paper](https://arxiv.org/pdf/2602.01090)

2. **ConRep4CO: Contrastive Representation Learning of Combinatorial Optimization Instances across Types** ICLR, 2026. [paper](https://openreview.net/forum?id=OXRnvOOiAf), [code](https://github.com/Thinklab-SJTU/ConRep4CO)
    *Ziao Guo, Yang Li, Shiyue Wang, Junchi Yan*

3. **ML4CO-Bench-101: Benchmark Machine Learning for Classic Combinatorial Problems on Graphs** NeurIPS, 2025. [paper](https://openreview.net/forum?id=ye4ntB1Kzi), [code](https://github.com/Thinklab-SJTU/ML4CO-Bench-101)
    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

4. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://neurips.cc/virtual/2025/loc/san-diego/poster/115835), [code](https://github.com/Summer142857/LLMCoSolver)
    *Xia Jiang, Yaoxin Wu, Minshuo Li, Zhiguang Cao, Yingqian Zhang*

5. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://arxiv.org/pdf/2509.16865), [code](https://github.com/Summer142857/LLMCoSolver)

6. **GraphThought: Graph Combinatorial Optimization with Thought Generation** Arxiv, 2025. [paper](https://arxiv.org/pdf/2502.11607)

7. **GraphArena: Evaluating and Exploring Large Language Models on Graph Computation** ICLR, 2025. [paper](https://openreview.net/pdf?id=Y1r9yCMzeA), [code](https://github.com/squareRoot3/GraphArena/tree/master)

8. **COExpander: Adaptive Solution Expansion for Combinatorial Optimization** ICML, 2025. [paper](https://openreview.net/forum?id=KMaBXMWsBM), [code](https://github.com/Thinklab-SJTU/COExpander)
    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

9. **Approximation algorithms for combinatorial optimization with predictions** ICLR, 2025. [paper](https://openreview.net/forum?id=AEFVa6VMu1)
    *Antonios Antoniadis, Marek Elias, Adam Polak, Moritz Venzin*

10. **Aligning LLMs with Graph Neural Solvers for Combinatorial Optimization** Under Review, 2025. [paper](https://openreview.net/pdf?id=KSfLDk3jxI)

11. **UNCO: Towards Unifying Neural Combinatorial Optimization through Large Language Model** Arxiv, 2024. [paper](https://arxiv.org/pdf/2408.12214)

12. **GOAL: A Generalist Combinatorial Optimization Agent Learner** ICLR, 2024. [paper](https://arxiv.org/pdf/2406.15079), [code](https://github.com/naver/goal-co)

