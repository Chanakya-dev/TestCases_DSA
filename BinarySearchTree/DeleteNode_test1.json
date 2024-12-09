{
  "code": "class Node:\n    def __init__(self, key):\n        self.key = key\n        self.left = None\n        self.right = None\n\ndef delete_node(root, key):\n    if not root:\n        return root\n\n    if key < root.key:\n        root.left = delete_node(root.left, key)\n    elif key > root.key:\n        root.right = delete_node(root.right, key)\n    else:\n        if not root.left:\n            return root.right\n        elif not root.right:\n            return root.left\n\n        temp = find_min(root.right)\n        root.key = temp.key\n        root.right = delete_node(root.right, temp.key)\n\n    return root\n\ndef find_min(node):\n    current = node\n    while current.left:\n        current = current.left\n    return current",
  "language": "python",
  "test_cases": [
    {
      "description": "Delete a leaf node (10)",
      "function_name": "delete_node",
      "input": {
        "root": {
          "key": 100,
          "left": {
            "key": 50,
            "left": {"key": 10, "left": null, "right": null},
            "right": {"key": 75, "left": null, "right": null}
          },
          "right": {
            "key": 200,
            "left": {"key": 150, "left": null, "right": null},
            "right": {"key": 250, "left": null, "right": null}
          }
        },
        "key": 10
      },
      "expected": {
        "key": 100,
        "left": {
          "key": 50,
          "left": null,
          "right": {"key": 75, "left": null, "right": null}
        },
        "right": {
          "key": 200,
          "left": {"key": 150, "left": null, "right": null},
          "right": {"key": 250, "left": null, "right": null}
        }
      },
      "name": "Test delete leaf node"
    },
    {
      "description": "Delete a node with one child (150)",
      "function_name": "delete_node",
      "input": {
        "root": {
          "key": 100,
          "left": {
            "key": 50,
            "left": {"key": 10, "left": null, "right": null},
            "right": {"key": 75, "left": null, "right": null}
          },
          "right": {
            "key": 200,
            "left": {"key": 150, "left": null, "right": null},
            "right": {"key": 250, "left": null, "right": null}
          }
        },
        "key": 150
      },
      "expected": {
        "key": 100,
        "left": {
          "key": 50,
          "left": {"key": 10, "left": null, "right": null},
          "right": {"key": 75, "left": null, "right": null}
        },
        "right": {
          "key": 200,
          "left": null,
          "right": {"key": 250, "left": null, "right": null}
        }
      },
      "name": "Test delete node with one child"
    },
    {
      "description": "Delete a node with two children (200)",
      "function_name": "delete_node",
      "input": {
        "root": {
          "key": 100,
          "left": {
            "key": 50,
            "left": {"key": 10, "left": null, "right": null},
            "right": {"key": 75, "left": null, "right": null}
          },
          "right": {
            "key": 200,
            "left": {"key": 150, "left": null, "right": null},
            "right": {"key": 250, "left": null, "right": null}
          }
        },
        "key": 200
      },
      "expected": {
        "key": 100,
        "left": {
          "key": 50,
          "left": {"key": 10, "left": null, "right": null},
          "right": {"key": 75, "left": null, "right": null}
        },
        "right": {
          "key": 250,
          "left": {"key": 150, "left": null, "right": null},
          "right": null
        }
      },
      "name": "Test delete node with two children"
    },
    {
      "description": "Delete the root node (100)",
      "function_name": "delete_node",
      "input": {
        "root": {
          "key": 100,
          "left": {
            "key": 50,
            "left": {"key": 10, "left": null, "right": null},
            "right": {"key": 75, "left": null, "right": null}
          },
          "right": {
            "key": 200,
            "left": {"key": 150, "left": null, "right": null},
            "right": {"key": 250, "left": null, "right": null}
          }
        },
        "key": 100
      },
      "expected": {
        "key": 150,
        "left": {
          "key": 50,
          "left": {"key": 10, "left": null, "right": null},
          "right": {"key": 75, "left": null, "right": null}
        },
        "right": {
          "key": 200,
          "left": null,
          "right": {"key": 250, "left": null, "right": null}
        }
      },
      "name": "Test delete root node"
    }
  ]
}
