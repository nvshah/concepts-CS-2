package com.company.WFDS.Queue;

/**
 * ref : https://raw.githubusercontent.com/williamfiset/Algorithms/master/src/main/java/com/williamfiset/algorithms/datastructures/queue/Queue.java
 */
public interface Queue<T> {
    public void offer(T elem);

    public T poll();

    public T peek();

    public int size();

    public boolean isEmpty();
}