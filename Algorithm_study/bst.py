# https://www.acmicpc.net/problem/5639

from sys import stdin 
input = stdin.readline

#트리를 구성하는 노드 클래스
class Node:
    """생성자"""
    def __init__(self, key,value, left,right):
        self.key = key      # 키
        self.value = value  # 값
        self.left = left    # 왼쪽 자식 참조
        self.right = right  # 오른쪽 자식 참조

class BST():	
    
    # 생성자
    def __init__(self)->None:
        self.root = None    # 루트 설정


    # 검색하는 메소드
    def search(self, key)->int:
        node = self.root # 루트에 주목
        while True:
            if node is None:    # 더 이상 진행할 수 없으면, 검색 실패
                return -1       
            if key == node.key: 
                return node.value 
            elif key < node.key:    # key가 노드보다 작으면, 왼쪽 서브 트리에서 검색
                node = node.left
            else:                   # key가 노드보다 크면, 오른쪽 서브 트리에서 검색
                node = node.right
    

    # 노드 추가하는 메소드
    def add(self,key,value)->bool:
        # 노드 추가하는 내부 함수
        def add_node(node,key,value)->None:
            if key == node.key:     #이미 삽입하려는 키가 있으면 false 처리
                return False

            elif key < node.key:    # key가 노드보다 작으면,
                if node.left is None:       # 노드의 왼쪽 자식이 없다면 바로 그 자리에 삽입
                    node.left = Node(key,value,None,None)
                else:                       # 자식이 있으면 재귀함수 호출로 한번 더 들어감
                    add_node(node.left,key,value)
            else:                   # key가 노드보다 크면,           
                if node.right is None:      # 노드의 오른쪽 자식이 없다면 바로 그 자리에 삽입
                    node.right = Node(key,value,None,None)
                else:                       # 자식이 있으면 재귀함수 호출로 한번 더 들어감
                    add_node(node.right,key,value)
            return True
        # root는 root에 대한 참조
        if self.root is None:       # 트리가 빈 상태이면, 루트만으로 구성된 트리를 만든다
            self.root = Node(key,value,None,None)
            return True
        else:
            return add_node(self.root,key,value)


    # 노드 삭제하는 메소드
    def remove(self, key)-> bool:
        node = self.root        # 현재 노드로 지정
        parent = None           # 현재 노드의 부모 노드
        is_left_child = True    # 현재 노드가 왼쪽 자식 노드인지 오른쪽 자식 노드인지 확인

        # 삭제할 노드 탐색
        while True:
            if node is None:    # 더이상 진행할 수 없으면
                return False
            if key == node.key: 
                break
            else:
                parent = node   # 가지를 내려가기 전에 부모를 설정
                if key < node.key:
                    node = node.left
                    is_left_child = True # 왼쪽 자식 노드로 내려가니까 플래그를 True로 설정
                else:
                    node = node.right
                    is_left_child = False # 오른쪽 자식 노드로 내려가니까 플래그를 True로 설정
            
        # 키를 찾은 뒤에 자식이 없는 노드이면 or 자식이 1개 있는 노드이면
        if node.left is None:       # 왼쪽 자식이 없으면
            if node is self.root:           # 만약 삭제 노드가 root이면, 바로 오른쪽 자식으로 대체한다.
                self.root = node.right
            # 아래의 parent는 탐색 시 찾은 노드의 바로 위 부모가 됨.(탐색 로직에서 그렇게 적용)
            # parent - node - node의 자식의 구도가 있으면 node라는 중간이 빠지기 때문에 parent의 자식과 node의 자식을 연결
            # (node의 자식이 없으면 자연스레 None이 들어감)
            elif is_left_child:             # 왼쪽 자식 노드가 있는 것이니까
                parent.left = node.right    # 부모의 왼쪽 참조가 오른쪽 자식을 가리킴
            else:                           # 오른쪽 자식 노드가 있는 것이니까
                parent.right = node.right   # 부모의 오른쪽 참조가 오른쪽 자식을 가리킴
        
        elif node.right is None:    # 오른쪽 자식이 없으면
            if node is self.root: 
                self.root = node.left       # 만약 삭제 노드가 root이면, 바로 왼쪽 자식으로 대체한다.
            elif is_left_child:
                parent.left = node.left     # 부모의 왼쪽 참조가 왼쪽 자식을 가리킴
            else:
                parent.right = node.left    # 부모의 오른쪽 참조가 왼쪽 자식을 가리킴


    # 노드 출력하는 메소드
    def dump(self)->None:
        def print_subtree(node):
            # 전위 순회로 출력
            if node is not None:
                print(f'{node.key} {node.value}')
                print_subtree(node.left)
                print_subtree(node.right)
        root = self.root
        print_subtree(root)



# 재귀

# 노드 생성과 삽입
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
class BinarySearchTree(Node):
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

# 노드 탐색
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

# 노드 삭제
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        # 해당 노드가 삭제할 노드일 경우
        if key == node.data:
            deleted = True
            # 삭제할 노드가 자식이 두개일 경우
            if node.left and node.right:
                # 오른쪽 서브 트리에서 가장 왼쪽에 있는 노드를 찾고 교체
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            # 자식 노드가 하나일 경우 해당 노드와 교체
            elif node.left or node.right:
                node = node.left or node.right
            # 자식 노드가 없을 경우 그냥 삭제
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted