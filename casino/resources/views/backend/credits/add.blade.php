@extends('backend.layouts.app')

@section('page-title', trans('app.add_credit'))
@section('page-heading', trans('app.add_credit'))

@section('content')
<section class="content-header">
	@include('backend.partials.messages')
</section>
<section class="content">
	<form action="{{ route('backend.credit.store') }}" method="POST" enctype="multipart/form-data" id="user-form">
		@csrf
		<div class="box box-default">
			<div class="box-header with-border">
				<h3 class="box-title">@lang('app.add_credit')</h3>
			</div>
			<div class="box-body">
				<div class="row">
					@include('backend.credits.partials.base', ['edit' => false, 'profile' => false])
				</div>
			</div>
			<div class="box-footer">
				<button type="submit" class="btn btn-primary">
					@lang('app.add_credit')
				</button>
			</div>
		</div>
	</form>
</section>
@stop

@section('scripts')
@stop