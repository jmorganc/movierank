%rebase('templates/layout.tpl', title='Movies', active_home='class="active"')
        <div class="page-header">
            <h1>Movies</h1>
        </div>

        <div class="row">
            <div class="col-md-12">
                See what movies are available and add them to your collection.
            </div>
        </div>

        <div class="row bottom_margin">
            <div class="col-md-12">
                <h2>Not in Collection</h2>
                %num_movies = len(movies_nic)
                %for i, movie in enumerate(movies_nic):
                %if i % 4 == 0:
                <div class="row">
                %end
                    <div class="col-md-3">
                        <div class="movie">
                            <img src="/img/movies/{{movie['title'].lower()}}.jpg" alt="{{movie['title']}}"/><br/>
                            <strong>{{movie['title']}}</strong><br/>
                            <strong>ID: </strong>{{movie['id']}}<br/>
                            <strong>In collection: </strong>{{movie['in_collection']}}<br/>
                            <a href="javascript:void(0);">Add</a>
                        </div>
                    </div>
                %if (i > 0 and (i+1) % 4 == 0) or i+1 == num_movies:
                </div>
                %end
                %end
            </div>
        </div>

        <div class="row bottom_margin" style="border-top: 1px solid #ddd;">
            <div class="col-md-12">
                <h2>In Collection</h2>
                %num_movies = len(movies_ic)
                %for i, movie in enumerate(movies_ic):
                %if i % 4 == 0:
                <div class="row">
                %end
                    <div class="col-md-3">
                        <div class="movie">
                            <img src="/img/movies/{{movie['title'].lower()}}.jpg" alt="{{movie['title']}}"/><br/>
                            <strong>{{movie['title']}}</strong><br/>
                            <strong>ID: </strong>{{movie['id']}}<br/>
                            <strong>In collection: </strong>{{movie['in_collection']}}<br/>
                            <a href="javascript:void(0);">Remove</a>
                        </div>
                    </div>
                %if (i > 0 and (i+1) % 4 == 0) or i+1 == num_movies:
                </div>
                %end
                %end
            </div>
        </div>