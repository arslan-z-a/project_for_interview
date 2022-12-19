from django.db import models


class TypesOfWorkDO(models.Model):
    """Виды работ ДО"""
    title = models.CharField(max_length=250, unique=True, verbose_name="Название вида работы: ")
    description = models.TextField(verbose_name="Cодержание работы: ")
    agreement = models.BooleanField(default=True, verbose_name="Активность")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Вид работы ДО"
        verbose_name_plural = "Виды работ ДО"


class TransgazList(models.Model):
    """Список трансгазов """
    title = models.CharField(max_length=100, unique=True, verbose_name="Название трансгаза:")
    number = models.IntegerField(unique=True, verbose_name="Номер трансгаза (X):")
    agreement = models.BooleanField(default=True, verbose_name="Активность")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Трансгаз"
        verbose_name_plural = "Список трансгазов"


class ActivitiesDO(models.Model):
    """Направления деятельности"""
    title = models.CharField(max_length=250, unique=True, verbose_name="Направление деятельности:")
    number = models.IntegerField(unique=True, verbose_name="Номер деятельности (Y):")
    description = models.TextField(verbose_name="Описание:")
    agreement = models.BooleanField(default=True, verbose_name="Активность")
    transgaz = models.ForeignKey('TransgazList', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Направление деятельности"
        verbose_name_plural = "Направления деятельности"


class StructuralSubdivision(models.Model):
    """структурные подразделения"""
    title = models.CharField(max_length=100, unique=True, verbose_name="Название структурного подразделения:")
    number = models.IntegerField(unique=True, verbose_name="Номер структурного подразделения:")
    agreement = models.BooleanField(default=True, verbose_name="Активность")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Структурное подразделение"
        verbose_name_plural = "Структурные подразделения"


class ReportingYear(models.Model):
    """Год"""
    year = models.IntegerField(max_length=4, unique=True, verbose_name="Отчетный год:")
    agreement = models.BooleanField(default=True, verbose_name="Активность")

    def __str__(self):
        return str(self.year)

    class Meta:
        ordering = ["year"]
        verbose_name = "Отчетный год"
        verbose_name_plural = "Отчетные года"


class AccountBalance(models.Model):
    """Счет в бухгалтерии"""
    title = models.CharField(max_length=100, unique=True, verbose_name="Название баоанса: ")
    agreement = models.BooleanField(default=True, verbose_name="Активность")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["agreement"]
        verbose_name = "Баланс"
        verbose_name_plural = "Балансы"


class Bookkeeping(models.Model):
    """Зона отвественности бухгалтерии"""
    title_obj_OC = models.CharField(max_length=250, verbose_name="Название объекта по ОС:")
    inventory_num = models.CharField(max_length=20, verbose_name="Инвентарный номер:")
    object_cost = models.DecimalField(max_digits=15, decimal_places=6, verbose_name="Стоимость объекта по бухгалтерии:")
    commissioning_date = models.DateField(verbose_name="Дата ввода в эксплуатацию:")
    account_balance = models.ForeignKey('AccountBalance', on_delete=models.PROTECT, verbose_name="Баланс")

    def __str__(self):
        return self.title_obj_OC

    class Meta:
        ordering = ["title_obj_OC"]
        verbose_name = "ОС бухгалтерия"
        verbose_name_plural = "ОС бухгалтерия"


class Lpumg(models.Model):
    """ЛПУМГ"""
    actual_object_name = models.CharField(max_length=250, verbose_name="Фактическое название объекта:")
    project_supporting_documentation = models.FileField(upload_to='Lpumg/doc', verbose_name="Проектная документация:")
    project_supporting_pdf = models.FileField(upload_to='Lpumg/pdf', verbose_name="Проектная документация в Pdf:")
    description = models.TextField(verbose_name="Комментарий:")
    agreement = models.BooleanField(default=True, verbose_name="Активность")
    date_of_download = models.DateTimeField(verbose_name="Дата загрузки обновляемая:")
    object_characteristics = models.TextField(verbose_name="Характеристика объекта:")
    structural_subdivision = models.ForeignKey('StructuralSubdivision', on_delete=models.PROTECT, verbose_name="Структурное подразделение:")
    activities_DO = models.ForeignKey('ActivitiesDO', on_delete=models.PROTECT)
    types_Of_Work_DO = models.ForeignKey('TypesOfWorkDO', on_delete=models.PROTECT)
    bookkeeping = models.ForeignKey('Bookkeeping', on_delete=models.PROTECT)

    class Meta:
        ordering = ["actual_object_name", "activities_DO", "types_Of_Work_DO"]
        verbose_name = "ЛПУМГ"
        verbose_name_plural = "ЛПУМГ"


class ProductionDepartment(models.Model):
    """Производственный отдел"""
    addition_to_the_documentation = models.FileField(upload_to='Production_Department/doc')
    description = models.TextField()
    agreement = models.BooleanField(default=True)
    objects_lpumg = models.ForeignKey('Lpumg', on_delete=models.PROTECT)

    class Meta:
        ordering = ["agreement"]
        verbose_name = "Производственный отдел"
