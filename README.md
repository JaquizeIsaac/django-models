## Django-models 

### LAB - Class 27 Project: django-models

### Author: Myyela Isaac

### Links and Resources - N/A

### Setup - N/A

### PORT - N/A

### DATABASE_URL - N/A

### How to initialize/run your application - 

- `python manage.py runserver`

### How to use your library

`pip install -r requirements.txt`,
`npm install`

### Tests How do you run tests?

`python manage.py test`

### Tested-

```    
    def test_snack_list_page_status_code(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # def test_snack_list_page_template(self):
    #     url = reverse('snacks_list')
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, 'snacks_list.html')

```

### Any tests of note? - N/A

### Describe any tests that you did not complete, skipped, etc - `test_snack_list_page_template()` , unable to test without setup