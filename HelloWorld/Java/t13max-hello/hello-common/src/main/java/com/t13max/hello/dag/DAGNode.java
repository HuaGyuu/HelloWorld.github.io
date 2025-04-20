package com.t13max.hello.dag;

import lombok.Getter;

/**
 * 有向无圈图的节点
 *
 * @param <T>
 * 
 * 其实T未必要实现Comparable接口。暂时先这样吧
 */
public class DAGNode<T extends Comparable<T>> implements Comparable<DAGNode<T> > {
	@Getter
	private final T obj;
	@Getter
	private final java.util.ArrayList<DAGNode<T> > prevs;
	@Getter
	private final java.util.ArrayList<DAGNode<T> > nexts;
	private final DAG<T> dag;


	DAGNode(T obj, DAG<T> dag) {
		super();
		this.obj = obj;
		prevs=new java.util.ArrayList<DAGNode<T> >();
		nexts=new java.util.ArrayList<DAGNode<T> >();
		this.dag=dag;
	}
	
	public DAGNode<T> addPrev(T name) {
		final DAGNode<T> p = dag.createNodeIfNotExist(name);

		if (!prevs.contains(p)) {
			prevs.add(p);
			p.nexts.add(this);
		}

		return this;
	}

	public DAGNode<T> addNext(T name) {
		final DAGNode<T> p = dag.createNodeIfNotExist(name);

		if (!nexts.contains(p)) {
			nexts.add(p);
			p.prevs.add(this);
		}

		return this;
	}
	

	@Override
	public int compareTo(DAGNode<T> o) {		
		return this.obj.compareTo(o.obj);
	}
	
	@Override
	public int hashCode() {
		return this.obj.hashCode();
	}

	@Override
	public boolean equals(Object obj) {
		if (obj == null) {
			return false;
		}

		if (this == obj) {
			return true;
		}

		if (!(obj instanceof DAGNode)) {
			return false;
		}

		return ((DAGNode<?>) obj).obj.equals(this.obj);
	}

}
