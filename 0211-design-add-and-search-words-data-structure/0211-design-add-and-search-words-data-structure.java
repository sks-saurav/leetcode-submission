class Node{
    Node[] child;
    boolean end;
    Node() {
        child = new Node[26];
        end = false;
    }
}

class WordDictionary {
    Node root;
    public WordDictionary() {
        root = new Node();
    }
    
    public void addWord(String word) {
        Node node = root;
        for(int i=0;i<word.length();i++){
            int idx = word.charAt(i)-'a';
            if(node.child[idx] == null){
                node.child[idx] = new Node();
            }
            node = node.child[idx];
        }
        node.end = true;        
    }

    
    public boolean search(String word) {
        return searchHelp(0, root, word);
    }

    public boolean searchHelp(int idx, Node node, String word) {
        if(node == null) return false;
        if(idx == word.length()) return node.end;

        if(word.charAt(idx) == '.'){
            for(int i=0;i<26;i++){
                if(searchHelp(idx+1, node.child[i], word)) return true;
            }
        } else {
            int nx = word.charAt(idx)-'a';
            if(searchHelp(idx+1, node.child[nx], word)) return true;
        }
        
        return false;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */