from rest_framework import  serializers
from core.models import Tag, Ingredient, Recipe

class TagSerializer(serializers.ModelSerializer):
    """"serializer for tag object"""
    class Meta:
        model = Tag 
        fields =('id', 'name')
        read_only_fields =('id',)

        
class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for ingredient object"""
    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    """Serialize a Recipe"""
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset = Ingredient.objects.all()
    )

    tag = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset= Tag.objects.all()
    )
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'ingredients', 'tag', 'time_minutes', 'price', 'link')
        read_only_fields = ('id',)

        
class RecipeDetailSerializer(RecipeSerializer):
    """Serialize a recipe detail"""
    ingredients = IngredientSerializer(many=True, read_only=True)
    tag = TagSerializer(many=True, read_only=True)

