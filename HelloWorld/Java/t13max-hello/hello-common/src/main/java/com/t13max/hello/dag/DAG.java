package com.t13max.hello.dag;
/**
 * 有向无圈图
 *
 * @param <T>
 */
public class DAG<T extends Comparable<T> > {
	public static interface IWalk<T extends Comparable<T> > {
		public void onNode(DAGNode<T> n);
	}

	private final java.util.TreeSet<DAGNode<T> > nodes;

	public DAG() {
		nodes = new java.util.TreeSet<DAGNode<T> >();
	}

	/**
	 * 不存在则创建。存在则返回
	 * 
	 * @param name
	 * @return
	 */
	public DAGNode<T>  createNodeIfNotExist(T name) {
		DAGNode<T>  n;
		if ((n = getNode(name)) != null)
			return n;
		n = new DAGNode<T> (name, this);
		nodes.add(n);
		return n;
	}

	/**
	 * 返回指定的节点
	 * 
	 * @param name
	 * @return
	 */
	public DAGNode<T>  getNode(T name) {
		for (final DAGNode<T>  n : nodes) {
			if (n.getObj().equals(name))
				return n;
		}
		return null;
	}

	/**
	 * 遍历图
	 * 
	 * @param w
	 */
	public void walk(IWalk<T> w) {
		final java.util.LinkedList<DAGNode<T> > walked = new java.util.LinkedList<DAGNode<T> >();
		for (final DAGNode<T>  n : nodes) {
			if (walked.contains(n))
				continue;
			DAGNode<T>  curr = n;
			while (true) {
				final java.util.LinkedList<DAGNode<T> > parents = new java.util.LinkedList<DAGNode<T> >();
				for(int i=0;i!=curr.getPrevs().size();){
					final DAGNode<T>  p=curr.getPrevs().get(i);
					if (walked.contains(p)){
						++i;
						continue;
					}
					if (parents.contains(p))
						throw new RuntimeException("找到循环, name: " + p.getObj());
					parents.push(curr);
					curr = p;
					i=0;
				}

				// curr没有父节点
				w.onNode(curr);
				walked.add(curr);

				if (!parents.isEmpty()) {
					curr = parents.pollLast();
					continue;
				} else {
					// 遍历next
					for (final DAGNode<T>  p : curr.getNexts()) {
						if (walked.contains(p))
							continue;
						curr=p;
					}
					break;
				}
			}
		}
	}

}
