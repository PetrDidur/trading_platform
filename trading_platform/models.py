from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', **NULLABLE)
    model = models.CharField(max_length=100, verbose_name='Model', **NULLABLE)
    market_date = models.DateField(verbose_name='Market date', **NULLABLE)
    supplier = models.ForeignKey('NetworkNode', on_delete=models.CASCADE, verbose_name='Supplier', **NULLABLE)
    debt_to_supplier = models.FloatField(verbose_name='Debt to supplier', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return f'{self.name}, {self.model}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class NetworkNode(models.Model):
    LEVEL_CHOICES = (
        (0, 'Factory'),
        (1, 'Retailer'),
        (2, 'Individual Entrepreneur'),
    )

    name = models.CharField(max_length=100, verbose_name='Name', **NULLABLE)
    contact_email = models.EmailField(verbose_name='Contact email', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Country', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='City', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='Street', **NULLABLE)
    house_number = models.CharField(max_length=100, verbose_name='House number', **NULLABLE)
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Level', **NULLABLE)
    products = models.ManyToManyField('Product', verbose_name='Products')
    is_supplier = models.BooleanField(default=False, verbose_name='Is supplier')

    def __str__(self):
        return f'{self.name}, {self.level} , product{self.products}'

    class Meta:
        verbose_name = 'Network node'
        verbose_name_plural = 'Network nodes'
